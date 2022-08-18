
from src.models.book import Book


# List of resources
async def index():
    return 'Book list'


# Specific resource
async def store(data: Book):
    return data


# Specific resource
async def show(id: int):
    strId = str(id)
    return 'Show ' + strId + "'s book"


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
