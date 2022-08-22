
from fastapi import HTTPException
from src.models.auth import Login
from src.models.student import Student
from src.services.hashing import Hashing
from src.services.student import *


# Register an account
async def register(data: Student):
    hashPassword = Hashing.get_password_hash(data.password)
    document = {
        'name': data.name,
        'email': data.email,
        'password': hashPassword
    }

    result = await createAccount(document)
    if not result:
        return HTTPException(422, {
            'status': False,
            'errors': {
                'email': 'Email already exist.'
            }
        })
    else:
        return HTTPException(201, {
            'status': True,
            'message': 'Account created.'
        })


# Login to account
async def login(data: Login):
    return data
