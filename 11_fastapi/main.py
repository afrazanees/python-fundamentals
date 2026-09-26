# Basic FastAPI Application

# Import the FastAPI class
from fastapi import FastAPI

# Create the application
app = FastAPI()

@app.get("/")
# This is a decorator. It tells FastAPI:
# When a client sends a GET request to "/", execute the function below.

# This is the Python function that handles the request
def home():
    return {"message": "Hello World!"} # FastAPI converts the Python dictionary into a JSON response.
