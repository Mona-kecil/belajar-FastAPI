from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    # username: str required length between 5 and 50 characters
    username: str = Field(..., min_length=5, max_length=50)
    # email EmailStr required
    email: EmailStr = Field(...)
    # age int required greater than 18
    age: int = Field(..., gt=18)


class PublicUser(BaseModel):
    username: str
    age: int


@app.post('/users', response_model=PublicUser)
async def create_user(user: User):
    return user


@app.get('/json')
async def custom_json_response():
    return JSONResponse(
        status_code=201,
        content={
            'message': 'Custom JSON response created!'
        })


@app.get('/html', response_class=HTMLResponse)
async def custom_html_response():
    return "<h1>Custom HTML response created!</h1>"


@app.get('/file', response_class=FileResponse)
async def custom_file_response():
    return '/home/matcha/langBasic/roadmap.md'
