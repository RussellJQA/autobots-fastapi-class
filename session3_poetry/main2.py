# https://fastapi.tiangolo.com/tutorial/path-params/

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# uvicorn main2:app --reload

# http://localhost:8000/items/qwertyuiop
#   will return:
# {"item_id" : "qwertyuiop"}

# The 'int' type will give you editor support inside of your function, with error checks, completion, etc.
@app.get("/int_items/{int_item}")
async def read_int2(int_item: int):
    return {"int_item": int_item}


# http://localhost:8000/int_items/3
#   will return:
# {"int_item" : 3}


@app.get("/int_item_plus2/{int_item}")
async def read_int(int_item: int):
    # Because of the above 'int' type annotation (and FastAPI), we don't need to do the following check:
    # if isinstance(int_item, int):
    #     return {"int_item_plus2": int_item + 2}
    return {"int_item_plus2": int_item + 2}


# http://localhost:8000/int_item_plus2/4
#   will return:
# {"int_item_plus2" : 6}

# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
