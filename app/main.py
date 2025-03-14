from fastapi import FastAPI, Depends, HTTPException
# from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import ProfileSchema, ResponseSchema
from .crud import create_profile, get_first_profile
from .database import get_db, create_tables  
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Profile API",
    description="Written with FastAPI.",
)

# Ensure database tables are created on startup
@app.on_event("startup")
async def startup():
    await create_tables()

# Allow all origins
origins = [
    "*",
]

# CORSMiddleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (e.g., Authorization)
)


# All routes 
@app.get("/")
async def info():
    return {
        "Programing Languange": "Python(FastAPI)",
        "Documentation": "/docs/",
        "Profile": "/profile/",
        # "Post": "/post/"
    }

# Apology to avoid_me - 27th Feb, 25 
@app.get("/apology")
async def apology_to_avoidme():
    return{
        "first_name":"Iyanu",
        "last_name":"Arowosola",
        "Track":"Backend",
        "Offense":"I didn't follow instructions in time.",
        "Apology":"I take full responsibity for my actions, and I determine to follow instructions as given my mentors."
    }


@app.post("/create/", response_model=ProfileSchema)
async def create_profile_endpoint(profile: ProfileSchema, db: AsyncSession = Depends(get_db)):
    created_profile = await create_profile(db, profile)  # Await the coroutine here
    return created_profile

@app.get("/profile", response_model=ResponseSchema)
async def read_first_profile(db: AsyncSession = Depends(get_db)):
    profile = await get_first_profile(db)  # Await the coroutine
    if profile is None:
        raise HTTPException(status_code=404, detail="No profiles found in the database")

    profile_data = ResponseSchema.from_orm(profile)
    profile_data.current_datetime = profile.current_datetime.isoformat().replace("+00:00", "Z")

    return profile_data

