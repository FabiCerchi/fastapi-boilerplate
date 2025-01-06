from typing import Optional

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    total_count: int
    limit: int
    offset: int
    current_page: int
    total_pages: int

class PaginationParams(BaseModel):
    limit: Optional[int] = Field(10, ge=1, description="Number of items to return")
    offset: Optional[int] = Field(0, ge=0, description="Number of items to skip")