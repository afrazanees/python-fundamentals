from fastapi import FastAPI

app = FastAPI()

# Path Parameter - Part of the URL path.
# If a user visits /products/10 in the GET endpoint below, 10 is extracted as the path parameter.

@app.get("/products/{id}")
def get_products(id: int):
    return {
        "product": id
    }
