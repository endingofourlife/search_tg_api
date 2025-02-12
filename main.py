from fastapi import FastAPI
from routes import api_v1_router

app = FastAPI(docs_url='/')

app.include_router(api_v1_router, prefix='/api/v1')
