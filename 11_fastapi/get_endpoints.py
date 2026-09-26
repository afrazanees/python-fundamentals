# Creating GET Endpoints

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "This is home"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "ABC"},
            {"id": 2, "name": "XYZ"},
            {"id": 3, "name": "PQR"}
        ]
    }


@app.get("/users/{user_id}")    # {user_id} is a path parameter.
def get_user(user_id: int):     
# :int is a Python type hint indicating user_id must be an integer.
# If the user visits /users/10, it is valid. Visiting /users/abc will return a "422 Unprocessable Entity" error.

    return{
        "users": user_id
    }
