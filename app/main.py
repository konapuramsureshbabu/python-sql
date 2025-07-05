from fastapi import FastAPI
from app.api.endpoints import auth, users
from app.db.database import engine
from app.db.models.user import Base

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Authentication App",
    description="A scalable FastAPI app with user authentication",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Authentication App"}