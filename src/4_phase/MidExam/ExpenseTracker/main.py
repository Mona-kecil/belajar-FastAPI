from fastapi import FastAPI
from models.connection import get_connection

app = FastAPI()


@app.get('/')
def root():
    return {'message': f'Hello from {__name__}!'}
