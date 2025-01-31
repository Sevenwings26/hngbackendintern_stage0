# Validate Data 
from pydantic import BaseModel, HttpUrl, validator
from datetime import datetime, timezone


class ProfileSchema(BaseModel):
    name: str
    email: str
    current_datetime: datetime
    github_url: str

    class Config:
        from_attributes = True  

    @validator("current_datetime")  # Ensure datetime is timezone-aware (UTC)
    def check_utc(cls, dt):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)  # Assume UTC if no timezone is provided.
        return dt


class ResponseSchema(BaseModel):
    email: str
    current_datetime: datetime
    github_url: str

    class Config:
        from_attributes = True  

