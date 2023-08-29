from time import sleep

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/add_numbers")
async def add_numbers(first, second):
    return float(first) + float(second)


@app.get("/multiple")
async def multiple(first, second):
    return float(first) * float(second)

@app.get("/subtraction_numbers")
async def subtraction_numbers(first: float, second: float):
    return first - second


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
# przejsc do folderu fastapi_app
# uvicorn app:app --reload
# ctrl c wyłączanie servera

