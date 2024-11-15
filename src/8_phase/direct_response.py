from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

app = FastAPI()


@app.get('/json')
def json_response():
    return JSONResponse({'message': 'Hello from JSONResponse!'})


@app.get('/html')
def html_response():
    return HTMLResponse('<h1>Hello from HTMLResponse!</h1>')


@app.get('/text')
def text_response():
    return PlainTextResponse('Hello from PlainTextResponse!')
