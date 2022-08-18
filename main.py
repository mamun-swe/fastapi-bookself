
from fastapi import FastAPI, Request
from src.routes.index import api_router

app = FastAPI()

app.include_router(api_router)

@app.get('/')
async def root(req: Request):
    hostname = req.base_url._url

    return {
        'message': 'Welcome to FastApi app.',
        'Sawgger documentation': hostname+'docs',
        'Alternative API docs': hostname+'redoc'
    }
