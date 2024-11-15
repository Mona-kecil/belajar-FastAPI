from fastapi import FastAPI, BackgroundTasks
import asyncio

app = FastAPI()


async def write_log(message: str):
    for i in range(len(message)):
        print(message[i], end='', flush=True)
        await asyncio.sleep(0.3)


@app.get('/')
async def root(text: str, background_tasks: BackgroundTasks):
    """
    Execution flow:
    1. Background task is added to the background tasks list.
    2. The function is executed asynchronously.
    3. The response is returned to the client without waiting for the background task to complete.
    """
    background_tasks.add_task(
        write_log, text)
    return {'message': f'Hello from {__file__}!'}
