from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.auth import router
from core.config import settings
from api.v1.endpoints.farmer import get_current_farmer

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(router, prefix=settings.API_V1_STR)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

v1 = FastAPI(
    dependencies=[Depends(get_current_farmer)],
)

app.mount("/v1", v1)

@app.get("/")
def root():
    return {"message": "Welcome to the Kaloka Recommendation System API"}
