
from fastapi import APIRouter, Depends
from src.controllers.student import *
from src.models.auth import Login
from src.models.student import Student
from src.middleware.permission import Permission


studentRouter = APIRouter(
    prefix='/student',
    tags=['Student'],
    dependencies=[Depends(Permission.student)],
    responses={404: {"message": "Route not found."}}
)


@studentRouter.post('/register')
async def registerAccount(data: Student):
    return await register(data)


@studentRouter.post('/login')
async def loginAccount(data: Login):
    return await login(data)
