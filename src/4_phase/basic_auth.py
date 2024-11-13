from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()
security = HTTPBasic()

VALID_USERS: list(dict({'username': str, 'password': str})) = [
    {'username': 'admin', 'password': 'admin'},
    {'username': 'user', 'password': 'user'}
]


def verify_credentials(credentials: HTTPBasicCredentials):
    for user in VALID_USERS:
        if (
            secrets.compare_digest(credentials.username, user['username']) and
            secrets.compare_digest(credentials.password, user['password'])
        ):
            return credentials.username
    raise HTTPException(status_code=401, detail='invalid credentials')


@app.get('/secure-data')
def secure_data(credentials: HTTPBasicCredentials = Depends(security)):
    username = verify_credentials(credentials)
    return {'message': f'Welcome, {username}!'}
