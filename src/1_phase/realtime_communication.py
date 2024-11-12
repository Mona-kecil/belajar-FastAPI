from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data.lower().startswith("hello"):
            await websocket.send_text("Hello to you too, my friend!")
            continue
        await websocket.send_text("Sorry, who is this?")
