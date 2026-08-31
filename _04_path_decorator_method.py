import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/get")
def get_test():
    return {"method": "get方法"}


@app.post("/post")
def post_test():
    return {"method": "post方法"}


@app.put("/put")
def put_test():
    return {"method": "put方法"}


@app.delete("/delete")
def delete_test():
    return {"method": "delete方法"}


if __name__=='__main__':
    uvicorn.run("_04_path_decorator_method:app",port=8080,log_level="debug",reload=True)
