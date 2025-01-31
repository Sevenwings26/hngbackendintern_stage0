
import asyncio
import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

Base = declarative_base()

DB_URL = config("DB_URL")

# Create an SSL context for asyncpg
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False  # Optional, depending on your security settings
ssl_context.verify_mode = ssl.CERT_NONE  # Change this to `ssl.CERT_REQUIRED` for full security

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



# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from decouple import config

# Base = declarative_base()

# # Use your Render PostgreSQL database URL
# DB_URL = "postgresql+asyncpg://hngstage0db_user:6qVTO2XIh0sySmksVIz8Zf8Mc7Bvnp4N@dpg-cuec0k5ds78s73abj0jg-a.oregon-postgres.render.com/hngstage0db?sslmode=require"

# # Async engine
# engine = create_async_engine(DB_URL, echo=True)

# # Async session factory
# SessionLocal = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False
# )

# # Function to create tables at startup
# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)  # Ensure tables are created

# # Dependency to get the DB session
# async def get_db():
#     async with SessionLocal() as session:
#         try:
#             yield session
#         finally:
#             await session.close()
