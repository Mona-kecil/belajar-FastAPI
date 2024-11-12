from fastapi import FastAPI
import httpx
import asyncio
import time

app = FastAPI()


@app.get("/messages")
async def get_messages():
    await asyncio.sleep(1)
    return {"messages": ["Hello there!", "Hi there!", "Greetings!"]}


@app.get("/todos")
async def get_todos():
    await asyncio.sleep(2)
    return {"todos": ["Buy milk", "Learn Python", "Go walk"]}


@app.get("/")
async def fetch_data():
    s = time.perf_counter()
    async with httpx.AsyncClient() as client:
        response1 = client.get("http://localhost:8000/messages")
        response2 = client.get("http://localhost:8000/todos")
        results = await asyncio.gather(response1, response2)
    e = time.perf_counter() - s
    return {
        "time_taken": f"Time taken to fetch all data is {e:.2f} seconds",
        "data": [result.json() for result in results]
    }
