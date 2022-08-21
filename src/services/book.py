
from src.config.database import database
from src.models.book import Book
from bson import ObjectId

# Database collection
collection = database.book


# Get all books
async def getAllBooks():
    items = []
    cursor = collection.find({})
    async for document in cursor:
        print(document['_id'])
        items.append(Book(**document))
    return items


# Create new book
async def createBook(data: Book):
    document = data.dict()
    result = await collection.insert_one(document)
    return result


# Find book by id
async def findBookById(id: str):
    result = await collection.find_one({'_id': ObjectId(id)})
    print(result)
    return {}
