from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'dipesh'}}


@app.get('/about')
def about():
    return {'data': {'name': 'dipesh'}}
