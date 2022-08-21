
from src.config.database import database
from src.models.book import Book
from bson import ObjectId

# Database collection
collection = database.book


# Get all books
async def getAllBooks():
    items = []
    cursor = collection.find().sort([('_id', -1)])
    async for document in cursor:
        items.append({
            **document,
            '_id': str(document['_id'])
        })
    return items


# Create new book
async def createBook(data: Book):
    document = data.dict()
    result = await collection.insert_one(document)
    return result


# Find book by id
async def findBookById(id: str):
    result = await collection.find_one({'_id': ObjectId(id)})
    return {
        **result,
        '_id': str(result['_id'])
    }


# Find book by id and update
async def findBookByIdAndUpdate(id: str, data: Book):
    document = data.dict()
    result = await collection.find_one({'_id': ObjectId(id)})
    if not result:
        return None

    await collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {**document}}
    )
    return True


# Find book by id and delete
async def findBookByIdAndDelete(id: str):
    result = await collection.find_one({'_id': ObjectId(id)})
    if not result:
        return None

    await collection.delete_one({'_id': ObjectId(id)})
    return True
