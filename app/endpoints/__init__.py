from fastapi import APIRouter
from app.endpoints import routes



router = APIRouter()

router.include_router(routes.router,tags=["main"])