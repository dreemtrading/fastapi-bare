from fastapi import FastAPI
from routes.someRoutes import class_router as SomeClassRouter
from contextlib import asynccontextmanager
from src.database.__connector__ import start_db


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await start_db()
    yield
    print('-> server has ended')

app = FastAPI(
    lifespan=app_lifespan,
    title="Dreem Trading Backend",
    description="Some description",
)

app.include_router(SomeClassRouter, )
