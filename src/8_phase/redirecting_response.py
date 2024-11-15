from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
import asyncio
app = FastAPI()


@app.get('/login')
async def login():
    await asyncio.sleep(2)
    return RedirectResponse(url='/')


@app.get('/register')
async def register():
    raise HTTPException(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
        headers={'Location': '/'})


@app.get('/')
async def root():
    return {'message': 'Hello from root!'}
