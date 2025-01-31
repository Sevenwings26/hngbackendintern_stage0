from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schema import ProfileSchema, ResponseSchema
from .crud import create_profile, get_first_profile
from .database import get_db  # Dependency for DB session
from .database import engine, Base  # Import Base from database.py


# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Profile API",
    description="Written with FastAPI.",
)

@app.get("/hello/")
async def info():
    return {"message": "FastAPI"}  


# Create profile
@app.post("/create/", response_model=ProfileSchema)
async def create_profile_endpoint(profile: ProfileSchema, db: Session = Depends(get_db)):
    return create_profile(db, profile)

# get first profile 
@app.get("/profile", response_model=ResponseSchema)
def read_first_profile(db: Session = Depends(get_db)):
    profile = get_first_profile(db)
    if profile is None:
        raise HTTPException(status_code=404, detail="No profiles found in the database")


    profile_data = ResponseSchema.from_orm(profile)
    profile_data.current_datetime = profile.current_datetime.isoformat().replace("+00:00", "Z")

    return profile_data
    # decorate 
    # return JSONResponse(content=profile_data.dict(), headers={
    #     "ContentType":"application/json"
    # })
