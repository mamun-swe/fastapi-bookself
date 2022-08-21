
# FastAPI Bookself application

This is a simple Bookself application like as CRUD built using Motor and FastAPI.

## Running the server

Set your [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/) as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.

```
ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net
DB_NAME=fastapi_bookself
```

Install the required dependencies:

```
python3 -m pip install -r requirements.txt
```

Start the server:
```
uvicorn main:app --reload
```

When the application starts, navigate to `http://localhost:8000/docs` and try out the `book` and `student` endpoints.
