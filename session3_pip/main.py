from typing import Optional

from fastapi import FastAPI


app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# IN TERMINAL:
# uvicorn main:app --reload

# IN BROWSER:
# http://127.0.0.1:8000/items/foo

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# IN TERMINAL:
# uvicorn main:app --reload

# IN BROWSER:
# http://127.0.0.1:8000/items/foo

# @app.get("/users/me")
# async def read_user_me(user_id: str):
#     return("user_id": "the current user")

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id + 2}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/hello")
# async def greeting(first_name: str, age: int):
#     return f"Hello, {first_name}, It looks like you are {age} years old"

# IN TERMINAL:
# uvicorn main:app --reload

# IN BROWSER:
# localhost:8000/hello?first_name=Russell&age=59
# http://localhost:8000/docs


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
