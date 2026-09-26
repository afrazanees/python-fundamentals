from fastapi import HTTPException, FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id > 99:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user_id
    }
