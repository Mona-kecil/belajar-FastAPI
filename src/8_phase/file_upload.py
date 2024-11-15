from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post('/upload')
async def uplaod(file: UploadFile = File(...)):
    return {
        'message': 'File uploaded successfully!',
        'file': file
    }
