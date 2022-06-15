from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

from pydantic import BaseModel, Field


class Paging(BaseModel):
    """Paging class."""

    page: int = Field(
        title="Current Page",
        description="The current page.",
        ge=0,
    )
    per_page: int = Field(
        title="Per Page",
        description="The number of items per page.",
        gt=0,
    )
    count: int = Field(
        title="Count on Page",
        description="The number of items on the current page.",
        ge=0,
    )
    total_count: int = Field(
        title="Total Count",
        description="The total number of items.",
        ge=0,
    )


class Album(BaseModel):
    """Album class."""

    id: int = Field(
        title="ID",
        description="The unique ID of the album.",
        ge=0,
    )
    name: Optional[str] = Field(
        title="Name",
        description="The name of the album.",
    )
    comment: Optional[str] = Field(
        title="Comment",
        description="The comment of the album.",
    )
    permalink: Optional[str] = Field(
        title="Permalink",
        description="The permalink of the album.",
    )
    status: Optional[str] = Field(
        title="Status",
        description="The status of the album.",
    )
    global_rank: Optional[str] = Field(
        title="Global Rank",
        description="The global rank of the album.",
    )
    nb_images: Optional[int] = Field(
        title="Number of Images",
        description="The number of images in the album.",
        ge=0,
    )
    total_nb_images: Optional[int] = Field(
        title="Total Number of Images",
        description="The total number of images in the album.",
        ge=0,
    )
    representative_picture_id: Optional[int] = Field(
        title="Representative Picture ID",
        description="The unique ID of the representative picture.",
    )
    date_last: Optional[datetime] = Field(
        title="Date Last",
        description="The date of the last modification of the album.",
    )
    max_date_last: Optional[datetime] = Field(
        title="Maximum Date Last",
        description="The latest date of the last modification of the album.",
    )
    nb_albums: Optional[int] = Field(
        alias="nb_categories",
        title="Number of Albums",
        description="The number of albums in the album.",
        ge=0,
    )
    url: str = Field(
        title="URL",
        description="The URL of the album.",
    )


class Image(BaseModel):
    """Image class."""

    id: int = Field(
        title="Image ID",
        description="The unique ID of the image.",
        ge=0,
    )
    width: int = Field(
        title="Image Width",
        description="The width of the image.",
        ge=0,
    )
    height: int = Field(
        title="Image Height",
        description="The height of the image.",
        ge=0,
    )
    hit: int = Field(
        title="Image Hits",
        description="The number of hits the image has received.",
        ge=0,
    )
    file: str = Field(
        title="Image File",
        description="The file name of the image.",
    )
    name: str = Field(
        title="Image Name",
        description="The name of the image.",
    )
    comment: Optional[str] = Field(
        title="Image Comment",
        description="The comment of the image.",
    )
    date_creation: datetime = Field(
        title="Image Creation Date",
        description="The creation date of the image.",
    )
    date_available: datetime = Field(
        title="Image Available Date",
        description="The available date of the image.",
    )
    page_url: str = Field(
        title="Image Page URL",
        description="The URL of the image page.",
    )
    element_url: str = Field(
        title="Image URL",
        description="The URL of the image.",
    )
    derivatives: Dict = Field(
        title="Image Derivatives",
        description="The derivatives of the image.",
    )
    albums: List[Album] = Field(
        alias="categories",
        title="Image Albums",
        description="The albums of the image.",
    )


class ImageOrder(str, Enum):
    """Image order choices."""

    ID = "id"
    FILE = "file"
    NAME = "name"
    HIT = "hit"
    RATING = "rating_score"
    DATE_CREATION = "date_creation"
    DATE_AVAILABLE = "date_available"
    RANDOM = "random"
