
from src.routes.index import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_router)


@app.get('/')
async def root(req: Request):
    hostname = req.base_url._url

    return {
        'message': 'Welcome to FastApi app.',
        'Sawgger documentation': hostname+'docs',
        'Alternative API docs': hostname+'redoc'
    }
