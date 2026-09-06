import uvicorn
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import time


app = FastAPI()

# @app.middleware("http")
# async def MyCORSMiddleware(request:Request,call_next):
#     response = call_next(request)
#     response.headers["Access-Control-Allow-Origin"]="*"
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  # *：代表所有客户端
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.get("/user")
def get_user():
    return {
        "user": "current user"
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8030,
                reload=True,workers=1)

