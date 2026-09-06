from fastapi import  FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from setting import TORTOISE_ORM
from api.student import student_api

app = FastAPI()

app.include_router(student_api,prefix="/student",tags=["选课系统学生接口"])

#与fastapi同步执行
register_tortoise(
    app = app,
    config=TORTOISE_ORM
)

if __name__=='__main__':
    uvicorn.run(app,port=8080,log_level="debug",workers=1)
