""" This app is an API for DenseNet model predictions """

from fastapi import FastAPI
from .routers import predict

app = FastAPI()
app.include_router(predict.router)


@app.get("/")
async def root():
    """
    This is the landing page and is used to check the health
    of the app.
    """
    return {"message": "Health Test"}
