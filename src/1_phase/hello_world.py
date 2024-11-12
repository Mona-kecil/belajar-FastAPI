# Installing FastAPI without standard dependencies
# pip install fastapi uvicorn
# to run: uvicorn src.1_phase.main:app
# watch mode: append --reload flag

from fastapi import FastAPI

app = FastAPI()

messages = ['Hello there!', 'Hi there!', 'Greetings!']


@app.get('/')
def read_root():
    return {'message': 'Hello from the other side'}


@app.get('/messages')
def get_messages():
    return {'messages': messages}
