from environs import Env
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

env = Env()
env.read_env('.env')

DATABASE_URL = URL.create(
    drivername='postgresql+asyncpg',
    username=env.str('POSTGRES_USER'),
    password=env.str('POSTGRES_PASSWORD'),
    host=env.str('POSTGRES_HOST'),
    database=env.str('POSTGRES_DB'),
    port=5432
).render_as_string(hide_password=False)

engine = create_async_engine(DATABASE_URL, echo=True, poolclass=None)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
