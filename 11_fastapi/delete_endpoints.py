from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.delete("/users/{user_id}")
def del_user(user_id: int):
    return{
        "message": "User deleted",
        "user_id": user_id
    }

# In a real application, you would delete the user record from persistent storage (such as a database).
