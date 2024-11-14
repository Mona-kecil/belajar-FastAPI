from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

USER_DB = {
    'admin-token': {'username': 'admin', 'role': 'admin'},
    'editor-token': {'username': 'editor', 'role': 'editor'},
    'viewer-token': {'username': 'viewer', 'role': 'viewer'}
}


def authenticate_user(token: str):
    user = USER_DB.get(token)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid token')
    return user


def authorize_user(required_role: str):
    def _authorize_user(user=Depends(authenticate_user)):
        if user['role'] != required_role:
            raise HTTPException(status_code=403, detail='Forbidden')
        return user
    return _authorize_user


@app.get('/admin')
def admin_route(user=Depends(authorize_user('admin'))):
    return {'message': f'Welcome, {user["username"]}, you have access to admin route'}


@app.get('/editor')
def editor_route(user=Depends(authorize_user('editor'))):
    return {'message': f'Welcome, {user["username"]}, you have access to editor route'}


@app.get('/viewer')
def viewer_route(user=Depends(authorize_user('viewer'))):
    return {'message': f'Welcome, {user["username"]}, you have access to viewer route'}

# To test:
# curl -H "Authorization: admin-token" http://localhost:8000/admin
