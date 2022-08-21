
from typing import List
from pydantic import BaseModel
from bson import ObjectId


class Book(BaseModel):
    _id: ObjectId()
    name: str
    title: str
    authors: List[str]
    tags: List[str]
    description: str
