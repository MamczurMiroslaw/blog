from fastapi import FastAPI

app = FastAPI()


# Creating an Endpoint to receive the data to make personalized greetings.
@app.post("/custom-greeting")
async def root(name):
    return {"message": f"Hello {name}"}
