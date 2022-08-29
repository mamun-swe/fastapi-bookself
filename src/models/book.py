
from typing import List
from pydantic import BaseModel


class Book(BaseModel):
    name: str
    title: str
    authors: List[str]
    tags: List[str]
    description: str
