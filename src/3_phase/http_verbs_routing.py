from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

greetings = dict(
    {
        1: 'Hello',
        2: 'Hi',
        3: 'Greetings',
        4: 'Bonjour',
        5: 'Hola',
        6: 'Ciao',
        7: 'こんにちは',
        8: '안녕하세요',
        9: '你好',
        10: 'Bonjour',
        11: 'Hallo',
        12: 'Hej',
        13: 'Olá',
        14: 'Здравствуйте',
        15: '您好',
    }
)


@app.get('/')
def read_root():
    """
    Define route for GET request to the root path '/'

    Response in JSON format
    """
    return {'message': f'Hello from {__file__}!'}


@app.get('/greetings/{greeting_id}')
async def get_greetings_by_id(greeting_id: Annotated[int, Path(ge=1, le=15)]):
    """
    Define route for GET request to the path '/greetings/{greeting_id}'

    Route parameters:
        greeting_id: int

    response in JSON format
    """
    return {'greeting': greetings.get(greeting_id)}


@app.get('/greetings')
async def get_greetings(limit: Annotated[int, Query(ge=1, le=15)] = 5, offset: Annotated[int, Query(ge=0)] = 0):
    """
    Define route for GET request to the path '/greetings'

    Query parameters:
        limit: int = 10
        offset: int = 0

    response in JSON format
    """
    if offset > len(greetings):
        return {'message':
                'Offset is greater than the total number of greetings'}

    if limit + offset > len(greetings):
        return {'message':
                'limit + offset is greater than the total number of greetings'}

    return {'greetings': list(greetings.values())[offset:limit]}
