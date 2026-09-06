from fastapi.exceptions import HTTPException
from typing import List

from fastapi import APIRouter
#导入模型类
from models import *
from pydantic import BaseModel
from watchfiles import awatch

student_api = APIRouter()

#ORM的查询操作
# 1.all()返回Queryset
# 2.filter(id=6)返回Queryset
# 3.get(id=6)返回Student()
# 4.模糊查询filter(id__gt=6)(gt为大于,不可直接写id>6)返回Queryset
#亦有id__range=[1,10000](划定范围)，id__in=[1001,1002](在其中返回)
#5.value查询：Queryset.value("name")返回对应dict的Queryset
#6.一对多查询 多对多查询

@student_api.get("/")
async def get_all_student():

    #一定要异步使用
    students = await Student.all().values("name","clas__name","courses__name")#用__查询外键
    #Queryset : [Student(),Student(),Student(),...]

    # for stu in students:
    #     #直接取外键对象
    #     print(await stu.clas.values("name"))


    return {
        "查看所有学生":students
    }

@student_api.get("/{stu_id}")
async def get_one_student(stu_id:int):

    stu = await Student.get(id=stu_id)
    print(await stu.courses.all().values("name","teacher__name","courses__name"))

    return {
        f"查找id={stu_id}的学生":stu
    }

#添加数据校验
class Student_in(BaseModel):
    sno:int
    pwd:int
    name:str
    clas_id:int
    courses:List[int]=[]
    #可加字段校验validator

@student_api.post("/")
async def add_student(student_in:Student_in):

    #插入数据库
    #方式1
    # stu = Student(name=student_in.name,
    #         pwd=student_in.pwd,
    #         sno=student_in.sno,
    #         clas_id=student_in.clas_id)
    #插入到数据库(数据库操作都需要异步)
    # await stu.save()

    #方式二
    stu = await Student.create(name=student_in.name,
            pwd=student_in.pwd,
            sno=student_in.sno,
            clas_id=student_in.clas_id)

    #多对多的关系绑定
    chosen_courses=await Course.filter(id__in=student_in.courses)
    await stu.courses.clear()#清除已有项
    await stu.courses.add(*chosen_courses)

    return {
        "添加一个学生":stu
    }

@student_api.put("/{stu_id}")
async def update_student(stu_id:int,stu_in:Student_in):

    data = stu_in.model_dump()
    #pop多对多字段
    courses = data.pop("courses")

    #更新数据
    await Student.filter(id=stu_id).update(**data)

    #设置多对多选修课
    edit_stu = await Student.get(id=stu_id)
    chosen_sourses=await Course.filter(id__in=courses)
    await edit_stu.courses.clear()
    await edit_stu.courses.add(*chosen_sourses)

    return {
        f"更新id={stu_id}的学生":edit_stu
    }

@student_api.delete("/{stu_id}")
async def delete_student(stu_id:int):

    deleteCount = await Student.filter(id=stu_id).delete()
    #同时删掉级联的多对多表

    if not deleteCount:
        #异常处理
        raise HTTPException(status_code=404,detail="Not Found")

    return {
        "操作":f"删除id={stu_id}的学生"
    }





