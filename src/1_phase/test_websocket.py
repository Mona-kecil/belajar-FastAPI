import asyncio
import websockets
import time


async def main():
    uri = 'ws://localhost:8000/ws'
    async with websockets.connect(uri) as ws:
        await ws.send('Hello, my friend!')
        s = time.perf_counter()
        response = await ws.recv()
        e = time.perf_counter() - s
        print(f"Time taken to receive response: {e:.8f} seconds")
        print(f"Response from server: {response}")

if __name__ == '__main__':
    asyncio.run(main())
