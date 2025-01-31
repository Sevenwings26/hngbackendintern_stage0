from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Profile
from .schema import ProfileSchema


# crete 
async def create_profile(db: AsyncSession, profile_data: ProfileSchema):
    query = select(Profile).where(Profile.email == profile_data.email)
    result = await db.execute(query)
    existing_profile = result.scalars().first()

    if existing_profile:
        return existing_profile

    # Ensure `current_datetime` is ISO 8601 (UTC)
    naive_datetime = profile_data.current_datetime.replace(tzinfo=None)

    new_profile = Profile(
        name=profile_data.name,
        email=profile_data.email,
        current_datetime=naive_datetime,
        github_url=profile_data.github_url
    )
    db.add(new_profile)
    await db.commit()
    await db.refresh(new_profile)
    return new_profile


# read
async def get_first_profile(db: AsyncSession):
    query = select(Profile)
    result = await db.execute(query)
    return result.scalars().first()


# Work on Update and Delete 
