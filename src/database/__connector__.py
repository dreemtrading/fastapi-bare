from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

database_url = f'{Config.DB_CONN}+aiomysql://{Config.DB_USER}:{Config.DB_PWD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}'
engine = AsyncEngine(
    create_engine(
        url=database_url,
        echo=True  # set this to true only on debugging
    )
)


async def start_db():
    async with engine.begin() as conn:
        try:
            # register all tables here
            from . import models

            await conn.run_sync(SQLModel.metadata.create_all)
        finally:
            await conn.close()  # Close the connection explicitly


async def get_session() -> AsyncSession:  # type: ignore
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
