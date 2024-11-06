from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - cursor-coll-a21606d6ed60434db8c030af99e34994',debug=False,docs_url='/silly-lamport-05b99c329c1711ef92d60242c0a8900343/docs',openapi_url='/silly-lamport-05b99c329c1711ef92d60242c0a8900343/openapi.json')

app.include_router(router, prefix='/silly-lamport-05b99c329c1711ef92d60242c0a8900343/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()