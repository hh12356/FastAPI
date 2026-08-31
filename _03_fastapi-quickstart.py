from fastapi import  FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return{"user_id":1001}

@app.get("/shop")
async def shop():
    return{"shopList":"..."}

if __name__=='__main__':
    uvicorn.run("_03_fastapi-quickstart:app",port=8080,log_level="debug",reload=True)
