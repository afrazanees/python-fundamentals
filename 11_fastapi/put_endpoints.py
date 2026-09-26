from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "id": user_id,
        "updated_user": user
    }


# NOTE:
# Right now, the above endpoint is an echo endpoint.
# It receives the data, validates it, and sends it straight back. 
# Nothing is permanently saved or modified because there is no storage layer 
# (such as a database or an in-memory dictionary) connected to it yet.
