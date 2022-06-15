import httpx
from httpx import Cookies
from pydantic import BaseModel

from .models.album import (
    GetAlbumImagesRequest,
    GetAlbumImagesResponse,
    GetAlbumListRequest,
    GetAlbumListResponse,
)
from .models.extra import Album, Image, Paging
from .models.images import AddImageRequest


class PiwigoClient:
    format = "json"

    def __init__(self, url: str, username: str, password: str):
        self.url = url + "/ws.php"
        self.username = username
        self.password = password
        self.logged_in = False
        self.cookies = Cookies()

        self._login()

    def _login(self):
        response = httpx.post(
            self.url,
            params={"format": self.format, "method": "pwg.session.login"},
            data={"username": self.username, "password": self.password},
        )
        response_dict = response.json()

        if response_dict["stat"] == "fail":
            raise PiwigoError(response_dict["message"], response_dict["err"])

        self.cookies = response.cookies

        if "pwg_id" not in self.cookies:
            raise PiwigoError("could not obtain user session id")

        self.logged_in = True

    def _make_request(self, http_method: str, method: str, request: BaseModel):
        try:
            params = {
                "format": self.format,
                "method": method,
                **request.dict(exclude_unset=True, exclude={"image_file"}),
            }
            files = None
            if "image_file" in request.__fields__:
                files = {"image": request.__getattribute__("image_file").open("rb")}
            response = httpx.request(
                http_method, self.url, params=params, files=files, cookies=self.cookies
            )
            response_json = response.json()
        except httpx.HTTPError as e:
            raise PiwigoError(str(e))
        if response_json["stat"] == "fail":
            raise PiwigoError(response_json["message"], response_json["err"])
        return response_json

    def get_album_list(self, request: GetAlbumListRequest) -> GetAlbumListResponse:
        method = "pwg.categories.getList"
        http_method = "GET"
        response = self._make_request(http_method, method, request)
        return GetAlbumListResponse(
            albums=[Album(**i) for i in response["result"]["categories"]]
        )

    def get_album_images(
        self, request: GetAlbumImagesRequest
    ) -> GetAlbumImagesResponse:
        method = "pwg.categories.getImages"
        http_method = "GET"
        response = self._make_request(http_method, method, request)
        return GetAlbumImagesResponse(
            paging=Paging(**response["result"]["paging"]),
            images=[Image(**i) for i in response["result"]["images"]],
        )

    def add_image(self, request: AddImageRequest):
        method = "pwg.images.addSimple"
        http_method = "POST"
        response = self._make_request(http_method, method, request)
        return response.json()


class PiwigoError(Exception):
    def __init__(self, error_message: str, status_code: int = None) -> None:
        self.error_message = error_message
        self.status_code = status_code

    def __str__(self) -> str:
        if self.status_code:
            return f"({self.status_code}) {self.error_message}"
        else:
            return self.error_message
