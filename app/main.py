from typing import Optional

from fastapi import FastAPI
# import RPi.GPIO as GPIO


app = FastAPI()

# inpin = 4
# outpin = 17

# GPIO.setup(inpin,GPIO.IN)
# GPIO.setup(outpin,GPIO.OUT)


@app.get("/")
def read_root():
    # return {"Hello": "World", f'GPIO{inpin}': GPIO.input(inpin)}
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# @app.get("/on")
# def read_on():
#     GPIO.output(outpin,1)
#     return {f"GPIO{outpin}": 1}

# @app.get("/off")
# def read_off():
#     GPIO.output(outpin,0)
#     return {f"GPIO{outpin}": 0}