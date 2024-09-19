from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.auth import router
from core.config import settings
from api.v1.endpoints.farmer import router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(router, prefix='')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Kaloka Recommendation System API"}
