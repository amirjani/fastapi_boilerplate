from fastapi import FastAPI, Request

from app import models
from app.api import deps

app = FastAPI()


@app.middleware("http")
async def access_control_layer(
    self,
    request: Request,
    call_next
):
    print('shit')

