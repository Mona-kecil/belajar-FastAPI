from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the request before the request is processed
        print(f'incoming request: {request.method} {request.url}')

        # Modify request headers (add custom headers)
        request.state.custom_header = "Property of MonTech"

        # Start timer
        start_time = time.time()

        # Process request and get response
        response = await call_next(request)

        # Stop timer
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'response time: {elapsed_time:.2f} seconds')

        print(f'response status: {response.status_code}')

        return response


app.add_middleware(LoggingMiddleware)


@app.get('/')
async def root(request: Request):
    """
    Execution flow:
    Middleware pre-process, execute below function, middleware post-process
    """
    return {
        'message': f'Hello from {__file__}!',
        'custom_header': request.state.custom_header
    }
