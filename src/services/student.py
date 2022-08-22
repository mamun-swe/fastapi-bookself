
from src.config.database import database
from src.models.student import Student

# Database collection
collection = database.student


# Create new account
async def createAccount(data: Student):
    isEmailExist = await collection.find_one({'email': data['email']})
    if isEmailExist:
        return False

    result = await collection.insert_one(data)
    return result
