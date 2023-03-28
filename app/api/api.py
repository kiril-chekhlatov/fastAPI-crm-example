from api.endpoints import comment, login, major, region, student, user
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(region.router, prefix="/regions", tags=["regions"])
api_router.include_router(major.router, prefix="/majors", tags=["majors"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(
    comment.router, prefix="/comments", tags=["comments"])
api_router.include_router(
    student.router, prefix="/students", tags=["students"])
