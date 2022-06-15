from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from piwigo.models.extra import Album, Image, ImageOrder, Paging


class GetAlbumListRequest(BaseModel):
    """Request class for GetAlbumList."""

    cat_id: Optional[int] = Field(
        None,
        alias="album_id",
        title="Album ID",
        description="The unique ID of the album.",
        ge=0,
    )
    recursive: Optional[bool] = Field(
        None,
        title="Recursive",
        description="Whether to include subalbums.",
    )
    public: Optional[bool] = Field(
        None,
        title="Public",
        description="Whether to include public albums.",
    )
    tree_output: Optional[bool] = Field(
        None,
        title="Tree Output",
        description="Whether to include the tree structure.",
    )
    fullname: Optional[bool] = Field(
        None,
        title="Full Name",
        description="Whether to include the full name.",
    )


class GetAlbumListResponse(BaseModel):
    """Response class for GetAlbumImages."""

    albums: List[Album] = Field(
        title="Albums", description="The current user's albums."
    )


class GetAlbumImagesRequest(BaseModel):
    """Request class for GetAlbumImages."""

    cat_id: Optional[List[int]] = Field(
        None,
        alias="album_id",
        title="Album ID",
        description="The unique ID of the album.",
        ge=0,
    )
    recursive: Optional[bool] = Field(
        None,
        title="Recursive",
        description="Whether to include subalbums.",
    )
    per_page: Optional[int] = Field(
        100,
        title="Images Per Page",
        description="The number of images to return per page.",
        gt=0,
    )
    page: Optional[int] = Field(
        0,
        title="Current Page",
        description="The current page.",
        ge=0,
    )
    order: Optional[ImageOrder] = Field(
        None,
        title="Image Order",
        description="The order in which to return the images.",
    )
    f_min_rate: Optional[float] = Field(
        None,
        title="Minimum Rating",
        description="The minimum rating of the images.",
        gt=0,
        le=5,
    )
    f_max_rate: Optional[float] = Field(
        None,
        title="Maximum Rating",
        description="The maximum rating of the images.",
        gt=0,
        le=5,
    )
    f_min_hit: Optional[int] = Field(
        None,
        title="Minimum Hits",
        description="The minimum number of hits the images have received.",
        gt=0,
    )
    f_max_hit: Optional[int] = Field(
        None,
        title="Maximum Hits",
        description="The maximum number of hits the images have received.",
        gt=0,
    )
    f_min_ratio: Optional[float] = Field(
        None,
        title="Minimum Ratio",
        description="The minimum ratio of the images.",
        gt=0,
    )
    f_max_ratio: Optional[float] = Field(
        None,
        title="Maximum Ratio",
        description="The maximum ratio of the images.",
        gt=0,
    )
    f_min_date_available: Optional[datetime] = Field(
        None,
        title="Minimum Date Available",
        description="The earliest date the images were available.",
    )
    f_max_date_available: Optional[datetime] = Field(
        None,
        title="Maximum Date Available",
        description="The latest date the images were available.",
    )
    f_min_date_created: Optional[datetime] = Field(
        None,
        title="Minimum Date Created",
        description="The earliest date the images were created.",
    )
    f_max_date_created: Optional[datetime] = Field(
        None,
        title="Maximum Date Created",
        description="The latest date the images were created.",
    )


class GetAlbumImagesResponse(BaseModel):
    """Response class for GetAlbumImages."""

    paging: Paging = Field(
        title="Paging",
        description="The paging information.",
    )
    images: List[Image] = Field(
        title="Images",
        description="The images in the album.",
    )
