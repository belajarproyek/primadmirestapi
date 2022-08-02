from fastapi import FastAPI
from instansi_route import router as instansi_router

app = FastAPI()

app.include_router(instansi_router)

@app.get("/")
async def read_main():
    return {"message": "Hello Bigger Applications!"}