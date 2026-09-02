import os.path
from fastapi import APIRouter
from pydantic import BaseModel,Field,field_validator
from datetime import  date
from typing import List, Optional
from fastapi import File,UploadFile

app05 = APIRouter()

@app05.post("/file")
async def get_file(file:bytes=File()):
    #字节流数据:适合小文件上传
    print("file",file)
    return {
        "file":len(file)
    }


#上传多个文件
@app05.post("/files")
async def get_files(files:List[bytes]=File(...)):
    return {
        "file":len(files)
    }

#使用UploadFile
@app05.post("/upload_file")
async def get_file(file:UploadFile=File(...)):
    print("file",file)

    #保存到本地
    path = os.path.join("imgs",file.filename)
    with open(path,"wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "file":file.filename
    }

@app05.post("/upload_files")
async def get_files(files:List[UploadFile]=File(...)):
    return {
        "file":len(files)
    }
