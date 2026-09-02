from fastapi import APIRouter
from pydantic import BaseModel,Field,field_validator
from datetime import  date
from typing import List, Optional
from fastapi import Form

app04 = APIRouter()

@app04.post("/register")
async def reg(username:str=Form(),password:str=Form()):
    print(f"username:{username},password:{password}")
    return {
        "username":username
    }

