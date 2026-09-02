import os.path
from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import  date
from typing import List, Optional, Union
from fastapi import File,UploadFile,Request

app07 = APIRouter()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_time:Optional[str]=None

#输出过滤password
class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_time:Optional[str]=None

@app07.post("/user",response_model=UserOut)
#设置响应模型
def create_user(user:UserIn):
    #存到数据库
    return user


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
#排除未设置字段
#类似有exclude_none:排除值为None的字段
async def read_item(item_id: str):
    return items[item_id]

@app07.get("/items02/{item_id}", response_model=Item, response_model_exclude={"tax"})
#exclude={}过滤
async def read_item(item_id: str):
    return items[item_id]

@app07.get("/items03/{item_id}", response_model=Item, response_model_include={"name","price"})
#include={}保留
async def read_item(item_id: str):
    return items[item_id]
