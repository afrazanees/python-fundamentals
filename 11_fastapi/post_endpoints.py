# To send data to our API, you create a POST request/endpoint.
# Example:
# Suppose you want to create a user.
# The request could look like: POST /users
# with JSON body data:
# {
#     "name": "ABC",
#     "age": 21
# }

# We need a way to tell FastAPI what the incoming data should look like.
# That's where Pydantic comes in.

# Pydantic helps us:
# - Define expected data structure
# - Validate incoming request payloads
# - Convert compatible types automatically
# - Produce structured error responses on invalid data


# Pydantic Models:
# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# This defines the expected structure:
# User
#    ├── name → string
#    └── age  → integer

# Now you can use it in an endpoint:
# @app.post("/users")
# def create_user(user: User):
#     return user


# Working Example:

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "API is running!"
    }

@app.post("/users")
def create_user(user: User):
    return{
        "message": "User Created!",
        "User": user
    }
