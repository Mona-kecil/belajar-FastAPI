from fastapi import FastAPI, Depends, HTTPException
# APIKeyQuery and APIKeyCookie are also available
from fastapi.security import APIKeyHeader

app = FastAPI()

API_KEY_NAME_TEST = 'X-API-KEY'
VALID_API_KEYS_TEST: set = {'valid-key', 'another-valid-key'}
api_key_header = APIKeyHeader(name=API_KEY_NAME_TEST, auto_error=False)


def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail='Please provide API Key to access this site.'
        )
    if api_key not in VALID_API_KEYS_TEST:
        raise HTTPException(
            status_code=401,
            detail='Invalid API key'
        )
    return api_key


@app.get('/secure-data-header')
def secure_data(api_key: str = Depends(validate_api_key)):
    return {'message': 'Access granted!', 'api_key_used': api_key}
