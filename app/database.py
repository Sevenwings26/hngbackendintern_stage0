
import asyncio
import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

Base = declarative_base()

DB_URL = config("DB_URL")

# SSL context for asyncpg
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False 
ssl_context.verify_mode = ssl.CERT_NONE

# Async engine with SSL
engine = create_async_engine(DB_URL, echo=True, connect_args={"ssl": ssl_context})

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

