import os.path
from fastapi import APIRouter
from pydantic import BaseModel,Field,field_validator
from datetime import  date
from typing import List, Optional
from fastapi import File,UploadFile,Request

app06 = APIRouter()

@app06.post("/items")
async def get_file(request:Request):

    print("URL:",request.url)
    print("IP:", request.client.host)
    print("agent:", request.headers.get("user_agent"))
    print("cookie:", request.cookies)

    return {
        "URL": str(request.url),
        "IP": request.client.host,
        "agent": request.headers.get("user-agent"),
        "cookie": request.cookies
    }
