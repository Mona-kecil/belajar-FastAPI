from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def generate_numbers():
    for i in range(10):
        yield f'Number {i}\n'
        await asyncio.sleep(1)


@app.get('/')
async def root():
    return StreamingResponse(generate_numbers(), media_type='text/event-stream')
