
from fastapi import HTTPException
from src.models.book import Book
from src.services.book import *


# List of resources
async def index():
    documents = await getAllBooks()
    return {
        'status': True,
        'data': documents
    }


# Store new resource
async def store(data: Book):
    result = await createBook(data)
    if result:
        return {
            'status': True,
            'message': 'Book created.'
        }
    return HTTPException(501, 'Something going to creating book.')


# Show specific resource
async def show(id: str):
    result = await findBookById(id)
    return result


# Update specific resource
async def update(id: int, data: Book):
    return {
        'id': id,
        'data': data
    }


# Destroy specific resource
async def destory(id: int):
    return {
        'id': id
    }
