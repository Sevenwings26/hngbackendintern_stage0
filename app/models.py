from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from .database import Base

class Profile(Base):

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    current_datetime = Column(DateTime, default=datetime.now(timezone.utc))
    github_url = Column(String, nullable=True)


