from fastapi import FastAPI

#create app
app = FastAPI()

#create endpoint
@app.get("/")
def index():
    return {"name": "First Data"}

