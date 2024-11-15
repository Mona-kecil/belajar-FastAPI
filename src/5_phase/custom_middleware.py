from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.middleware.base import BaseHTTPMiddleware
import time
import secrets
import logging

app = FastAPI()
security = HTTPBasic()

admin = {
    'username': 'admin',
    'password': 'password'
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.middleware('http')
async def log_request(request: Request, call_next: callable):
    """
    Global middleware for logging requests
    """
    logger.info(f'Incoming request: {request.method} {request.url}')
    s = time.perf_counter()
    response = await call_next(request)
    e = time.perf_counter() - s
    logger.info(
        f'Response status: {response.status_code}, response time: {e:.2f} seconds')
    return response


@app.get('/')
async def root(request: Request):
    return {
        'message': f'Hello from {__file__}!'
    }
