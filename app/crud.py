from sqlalchemy.orm import Session
from .models import Profile
from .schema import ProfileSchema

def create_profile(db: Session, profile_data: ProfileSchema):
    existing_profile = db.query(Profile).filter(Profile.email == profile_data.email).first()

    if existing_profile:
        return existing_profile 
    new_profile = Profile(
        name=profile_data.name,
        email=profile_data.email,
        current_datetime=profile_data.current_datetime,
        github_url=profile_data.github_url
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


def get_first_profile(db: Session) -> Profile:
    return db.query(Profile).first()


