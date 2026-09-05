from fastapi import  FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from setting import TORTOISE_ORM

app = FastAPI()

#与fastapi同步执行
register_tortoise(
    app = app,
    config=TORTOISE_ORM
)

if __name__=='__main__':
    uvicorn.run(app,port=8080,log_level="debug",workers=1)
