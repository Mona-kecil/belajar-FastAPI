from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()

# calling this function will automatically fetch the credentials from the request headers
security = HTTPBasic()

VALID_USER = {
    'username': 'matcha',
    'password': 'best flavor in the world'
}


def verify_credentials(credentials: HTTPBasicCredentials):
    if (
        secrets.compare_digest(credentials.username, VALID_USER['username']) and
        secrets.compare_digest(credentials.password, VALID_USER['password'])
    ):
        return credentials.username
    raise HTTPException(status_code=401, detail='invalid credentials')


@app.get('/secure-data')
def secure_data(credentials: HTTPBasicCredentials = Depends(security)):
    """
    This function will automatically call security function which fetch the credentials from the request headers
    """

    # pass the credentials to the verify_credentials function
    username = verify_credentials(credentials)
    return {'message': f'Welcome, {username}!'}
