from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Creating class to define the request body and the type hints of each attribute
class GreetingRequest(BaseModel):
    name: str


@app.post("/custom-greeting")
async def root(name: GreetingRequest):
    return {"message": f"Hello {name.name}"}
