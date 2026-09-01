from fastapi import APIRouter

app01 = APIRouter()

#按顺序路由匹配，由上向下
@app01.get("/user/1")
def get_user():
    return{
        "user_id":"root user"
    }

@app01.get("/user/{id}")
# 传递参数是字符串str类型
def get_user(id:int):
    #限制参数id类型,无法转化为对应类型会报错422
    return{
        "user_id":id
    }

