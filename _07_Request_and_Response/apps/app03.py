from fastapi import APIRouter
from pydantic import BaseModel,Field,field_validator
from datetime import  date
from typing import List, Optional

app03 = APIRouter()

#数据校验（前端传来的）
class User(BaseModel):
    #BaseModel自动调用请求体，而非url中的参数
    name:str
    age:int = Field(default=0,gt=-1,lt=100)#范围检测
    #类型不一致->类型转换->转换不成功报错
    birth:Optional[date]=None
    friendList:List[int]=[]
    description:Optional[str]=None

    @field_validator("name")
    def name_must_alpha(cls,value):
        assert value.isalpha(),'name must be alpha'
        return value

@app03.post("/data")
async def data(user:User):
    print(user)
    return user

