import socket

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/items",tags=["这是items的测试接口"],
          summary="this is items测试 summary",
          description="this is items测试详情",
          response_description="this is items测试 response_description",
          deprecated=True
          )
def test():
    return {"items": "items数据"}

if __name__=='__main__':
    uvicorn.run("_05_path_decorator_params:app",port=8080,log_level="debug",reload=True)

