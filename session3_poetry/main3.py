# https://fastapi.tiangolo.com/tutorial/query-params/

from typing import Optional

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# uvicorn main3:app --reload

# http://localhost:8000/items/?skip=0&limit=10
#   skip == "0", but 'int' type annotation causes FastAPI to convert to an int
#   limit == "10", but 'int' type annotation causes FastAPI to convert to an int

# http://localhost:8000/items/
#   equivalent to previous route, because of read_item()'s default values


@app.get("/hello/")
@app.get("/hello")  # equivalent
async def greeting(name1: str, age: int):
    return f"Hello, {name1}. It looks like you are {age} years old."


# http://localhost:8000/hello/?name1=Russell&age=25
#    "Hello, Russell. It looks like you are 25 years old."

# http://localhost:8000/hello/?age=25&name1=Russell
#   Same results, since the order of named parameters doesn't matter


@app.get("/hello2/")
async def greeting2(
    age: int, name1: str = "Daniel"  #
):  # Python requires arguments with default values to be last
    return f"Hello, {name1}. It looks like you are {age} years old."


# http://localhost:8000/hello2/?age=25
#    "Hello, Russell. It looks like you are 25 years old."


# http://localhost:8000/items3/hello?q=russell
#   {"item_id":"hello","q":"russell"}

# http://localhost:8000/items3/hello
#   { "item_id": "hello" }


@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# http://localhost:8000/items2/qwerty
#    { "item_id": "qwerty" }

# http://localhost:8000/items2/qwerty/?q=uiop
#    {"item_id":"qwerty","q":"uiop"}


@app.get("/items3/{item_id}")
async def read_item3(item_id: str, q: str = ""):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# http://localhost:8000/items3/qwerty3
#    { "item_id": "qwerty3" }

# http://localhost:8000/items3/qwerty3/?q=uiop
#    {"item_id":"qwerty3","q":"uiop"}


# See https://fastapi.tiangolo.com/tutorial/query-params/#query-parameter-type-conversion
#   1, True, true, on, yes, TRUE, Yes, etc. will all be treated as True

# See https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters
