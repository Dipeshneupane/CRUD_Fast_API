from fastapi import FastAPI
import models
from database import engine
import router
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def Home():
    return "Welcome Home"


app.include_router(router.router, prefix="/book", tags=['book'])
