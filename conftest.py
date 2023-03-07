"""Pytest configuration File"""
import asyncio
import pytest_asyncio
from httpx import AsyncClient
from mongomock_motor import AsyncMongoMockClient
from app.application import app
import seed_db


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Fixture to capture event loop for the test session"""
    yield asyncio.get_event_loop()


@pytest_asyncio.fixture(name="client")
async def client_fixture():
    """Creates a async client to be used with test"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(name="mongo_mock", autouse=True)
async def mongo_mock_fixture(monkeypatch):
    """Creates the mock for mongo database"""
    client = AsyncMongoMockClient()["where_to_eat"]
    col = client["restaurants"]
    await col.insert_many(seed_db.data[:2])

    def mocked_database():
        return client

    monkeypatch.setattr("app.database.where_to_eat", mocked_database)
