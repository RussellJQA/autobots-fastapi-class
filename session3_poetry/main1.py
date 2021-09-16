# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # Use root path
async def root():
    return {"message": "Hello from root"}


# In the shell (virtual environment in the Terminal):
# poetry shell
# uvicorn main1:app --reload
#    or just:
# poetry run uvicorn main1:app --reload

# In the browser:
# http://127.0.0.1:8000
#   or:
# http://localhost:8000


# To see documentation:
# http://localhost:8000/docs  # Documentation from Swagger.io API (Open API)
#   or alternative documentation at:
# http://127.0.0.1:8000/redoc


@app.get("/api")
async def api():
    return {1}


# http://localhost:8000/api

# You can't just do the following from the browser.
# You'd need to use Postman, Insomnia, or ...
# @app.post("/post-something")
# async def post_something():
#     return {"Hello"}
