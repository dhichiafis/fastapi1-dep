from fastapi import APIRouter,FastAPI
import uvicorn

app=FastAPI()


@app.get('/')
async def home():
    return {"message":'this is simpole deployment'}

@app.get("/home")
async def our_home():
    return {"home":'this is getting real interesting '}

if __name__=="__main__":
   uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True,)