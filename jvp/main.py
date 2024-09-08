from fastapi import FastAPI
from enum import Enum

app=FastAPI()

@app.get("/", description="This is first route", deprecated=True)
async def root():
    return {"message":"hello world"}

@app.post("/")
async def post():
    return {"message": "hello from post"}

@app.put("/")
async def put():
    return {"message": "hello from put"}

@app.get("/users")
async def get_users():
    return {"message":"list route"}

#order of routes does matter during declaration
@app.get("/users/me")
async def get_current_user():
    return {"message": "this is current user"}

@app.get("/users/{user_id}")
async def get_user(user_id:str):
    return {"message":user_id}

class FoodEnum(str, Enum):
    fruits="fruits"
    vegetable="vegetables"
    dairy="dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetable:
        return {"message": food_name}
    if food_name.value == "fruits":
        return {"message":"fruits"}
    return {
        "food_name": food_name}