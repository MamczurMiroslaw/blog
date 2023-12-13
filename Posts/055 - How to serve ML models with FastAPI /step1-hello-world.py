from fastapi import FastAPI

# Creating FastAPI instance
app = FastAPI()


# Creating a decorator that specifies that the function below supports
# HTTP GET requests on the path "/".
@app.get("/")
async def root():
    return {"message": "Hello World"}
