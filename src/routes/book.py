
from fastapi import APIRouter
from src.controllers.book import *
from src.models.book import Book


bookRouter = APIRouter(
    prefix='/book',
    tags=['Books'],
    responses={404: {"message": "Route not found."}}
)


@bookRouter.get('/')
async def getAllBook():
    return await index()


@bookRouter.post('/')
async def storeBook(data: Book):
    return await store(data)


@bookRouter.get('/{id}')
async def getSingleBook(id: str):
    return await show(id)


@bookRouter.put('/{id}')
async def updateSingleBook(id: str, data: Book):
    return await update(id, data)


@bookRouter.delete('/{id}')
async def deleteSingleBook(id: str):
    return await destory(id)
