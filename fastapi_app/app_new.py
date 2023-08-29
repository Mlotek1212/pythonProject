from time import sleep

from fast_api import FastAPI

app_new = FastAPI()


@app_new.get("/")
async def root():
    return {"message": "Hello World"}