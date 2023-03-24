"""Test file for database methods"""
import uuid
import pytest

from app import database

pytestmark = pytest.mark.asyncio


async def test_get_all_data():
    """Testing get all data"""
    data = await database.get_all_restaurants()
    assert data != []
    assert len(data) == 2


async def test_get_by_uuid(valid_data):
    """Testing get by uuid"""
    data = await database.get_restaurant_by_uuid(valid_data["uuid"])
    assert data is not None
    assert data["uuid"] == valid_data["uuid"]
    assert data["name"] == valid_data["name"]


async def test_invalid_uuid():
    """Testing get uuid with invalid uuid"""
    data = await database.get_restaurant_by_uuid("123")
    assert data is None


async def test_get_by_name(valid_data):
    """Testing get by name"""
    data = await database.get_restaurant_by_name(valid_data["name"])
    assert data is not None
    assert data["uuid"] == valid_data["uuid"]
    assert data["name"] == valid_data["name"]


async def test_get_by_name_lower(valid_data):
    """Testing get by name with case sensitive data"""
    data = await database.get_restaurant_by_name(valid_data["name"].lower())
    assert data is not None
    assert data["uuid"] == valid_data["uuid"]
    assert data["name"] == valid_data["name"]


async def test_get_by_invalid_name():
    """Testing get by name with invalid name"""
    data = await database.get_restaurant_by_name("Zachy Zachy")
    assert data is None


async def test_add_restaurant():
    """Testing add restaurant"""
    data = {
        "name": "Archers Restaurant",
        "uuid": str(uuid.uuid4()),
        "category": "Grill",
        "info": {
            "address": "10000 Dolphin DR, Butler, PA 16002",
            "phoneNumber": "(724) 822-5634",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "11AM-9PM",
            "tues": "11AM-9PM",
            "wed": "11AM-9PM",
            "thurs": "Closed",
            "fri": "11AM-10PM",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 2,
    }
    await database.add_restaurant(data)
    created = await database.get_restaurant_by_uuid(data["uuid"])
    assert created is not None
    assert created == data


async def test_update_restaurant(valid_data):
    """Testing update restaurant"""
    await database.update_restaurant(valid_data["uuid"], {"name": "Changed the name"})
    data = await database.get_restaurant_by_uuid(valid_data["uuid"])
    assert data["name"] == "Changed the name"


async def test_delete_restaurant(valid_data):
    """Testing delete restaurant"""
    await database.delete_restaurant(valid_data["uuid"])
    data = await database.get_restaurant_by_uuid(valid_data["uuid"])
    assert data is None
