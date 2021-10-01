

from fastapi import APIRouter

from .heartbeat import router as heartbeatRouter
from .prediction import router as predictionRouter

api_router = APIRouter()
api_router.include_router(heartbeatRouter, tags=["health"], prefix="/health")
api_router.include_router(predictionRouter, tags=[
                          "prediction"], prefix="/model")
