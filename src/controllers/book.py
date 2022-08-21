
from fastapi import HTTPException
from src.models.book import Book
from src.services.book import *


# List of resources
async def index():
    documents = await getAllBooks()
    return HTTPException(200, {
        'status': True,
        'data': documents
    })


# Store new resource
async def store(data: Book):
    result = await createBook(data)
    if result:
        return HTTPException(200, {
            'status': True,
            'message': 'Book created.'
        })
    return HTTPException(501, 'Something going to creating book.')


# Show specific resource
async def show(id: str):
    result = await findBookById(id)
    return HTTPException(200, {
        'status': True,
        'data': result
    })


# Update specific resource
async def update(id: str, data: Book):
    result = await findBookByIdAndUpdate(id, data)
    if not result:
        return HTTPException(404, {
            'status': False,
            'message': 'Book not found.'
        })
    return HTTPException(200, {
        'status': True,
        'message': 'Book updated.'
    })


# Destroy specific resource
async def destory(id: str):
    result = await findBookByIdAndDelete(id)
    if not result:
        return HTTPException(404, {
            'status': False,
            'message': 'Book not found.'
        })
    return HTTPException(200, {
        'status': True,
        'message': 'Book deleted.'
    })
