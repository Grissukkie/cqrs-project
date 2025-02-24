import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.patients import Base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(
  engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
  async with async_session_maker() as session:
    yield session

async def init_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
