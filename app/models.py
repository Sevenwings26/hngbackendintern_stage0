# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Profile(Base):
#     __tablename__ = "profiles"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     current_datetime = Column(String, nullable=False)  # Store as ISO 8601 string
#     github_url = Column(String, nullable=True)


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    current_datetime = Column(DateTime(timezone=True), nullable=False)  # Store with timezone
    github_url = Column(String, nullable=True)
