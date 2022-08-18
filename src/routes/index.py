
from fastapi import APIRouter
from src.routes.book import bookRouter
from src.routes.student import studentRouter

api_router = APIRouter()
api_router.include_router(bookRouter)
api_router.include_router(studentRouter)
