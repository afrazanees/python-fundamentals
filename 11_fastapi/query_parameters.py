from fastapi import FastAPI

app = FastAPI()

# Query Parameter - Appears after the "?" in the URL.
# Example: 
# /users?limit=10 (where limit=10 is a query parameter)

@app.get("/users/")
def users(limit: int):
    return {
        "limit": limit
    }

# NOTE:
# In the current implementation, "limit" is a required query parameter because it has no default value 
# assigned. If a client visits /users without ?limit=..., FastAPI will return a 422 Unprocessable 
# Entity validation error.


# Multiple Query Parameters
# You can accept multiple query parameters:
# /products?category=laptop&limit=10

@app.get("/products")
def get_products(category: str, limit: int):
    return{
        "category": category,
        "limit" : limit
    }
