from pathlib import Path
from typing import Optional, List

from pydantic import BaseModel, Field


class AddImageRequest(BaseModel):
    """Request class for AddImage."""

    image_file: Path = Field(
        title="Image File Path",
        description="The file path of the image to be uploaded.",
    )
    category: Optional[int] = Field(
        None,
        alias="album_id",
        title="Album ID",
        description="The unique ID of the album where the image will be added.",
        ge=0,
    )
    name: Optional[str] = Field(
        None,
        title="Name",
        description="The name of the image.",
    )
    author: Optional[str] = Field(
        None,
        title="Author",
        description="The author of the image.",
    )
    comment: Optional[str] = Field(
        None,
        title="Comment",
        description="The comment of the image.",
    )
    tags: Optional[List[str]] = Field(
        None,
        title="Tags",
        description="The tags of the image.",
    )
    image_id: Optional[int] = Field(
        None,
        title="Image ID",
        description="The unique ID of the image for overwriting an existing image.",
        ge=0,
    )
