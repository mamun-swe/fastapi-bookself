
from src.models.auth import Login
from src.models.student import Student
from src.services.hashing import Hashing


# Register an account
async def register(data: Student):

    hashPassword = Hashing.get_password_hash(data.password)
    return {
        'name': data.name,
        'email': data.email,
        'password': data.password,
        'hash_password': hashPassword
    }


# Login to account
async def login(data: Login):
    return data
