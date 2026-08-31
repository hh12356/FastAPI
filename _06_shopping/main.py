import socket

import uvicorn
from fastapi import FastAPI
from apps.app01.uris import shop
from apps.app02.uris import user

app = FastAPI()

app.include_router(shop,prefix="/shop",tags=["购物中心接口"])
app.include_router(user,prefix="/user",tags=["用户中心接口"])

if __name__=='__main__':
    uvicorn.run("main:app",port=8080,log_level="debug",reload=True)

