from fastapi import APIRouter
from typing import  Union,Optional

app02 = APIRouter()

@app02.get("/jobs/{kd}")
async def get_jobs(kd,xl:Union[str,None]=None,gj:Optional[str]=None):#有默认参数即选填值
    #路径参数：kd
    #不属于路径参数的其他参数自动解释为查询参数：xl,gj
    #查询参数：?后用&分割的键值对

    # Union类似联合体，变量类型二选一
    # Optional即Union自带None

    #数据库查询
    return {
        "kd":kd,
        "xl":xl,
        "gj":gj
    }

