from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel
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

#Path parameter
@app.get("/users/{user_id}")
async def get_user(user_id:str):
    return {"message":user_id}

class FoodEnum(str, Enum):
    fruits="fruits"
    vegetable="vegetables"
    dairy="dairy"

#Path parameter
@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetable:
        return {"message": food_name}
    if food_name.value == "fruits":
        return {"message":"fruits"}
    return {
        "food_name": food_name}

fake_items_db =[{"item":1}, {"item":2}, {"item":3}, {"item":4}, {"item":5}]

#Query Parameter
@app.get("/items")
async def list_items(skip:int=0, limit:int=10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def get_item(item_id:str, q:Optional[str]=None, short:Optional[bool]=False):
# async def get_item(item_id:str, q: str | None=None):
    item={"item_id": item_id}
    print("outside",item)
    if q:
        print("q", item)
        item.update({"q":q})
    if not short:
        print("short", item)
        item.update({"description":"slkdnf,mjbnsm"})
    print(item)
    return item

#multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}/")
async def get_user_items(user_id: int, item_id:str, q:Optional[str]=None, short:bool=False):
    item={"item_id": item_id, "owner_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc":"kdfhng,jmkbnfds"})
    return item

class Item(BaseModel):
    name:str
    desc:Optional[str]=None
    price:float
    tax:Optional[float]=None

#request body
@app.post("/items")
async def create_item(item:Item):
    # print(item.name)
    # print(item.desc)
    # print(item.tax)
    # print(item.price)
    item = item.dict()
    # print(item)
    if item["tax"] and item["price"]:
        item.update({"price_with_tax": item["price"] + item["price"]*item["tax"]/100})
    return item

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q:Optional[str]=None):
    item = {"item_id":item_id, **item.dict()}
    if q:
        item.update({"q":q})
    return item