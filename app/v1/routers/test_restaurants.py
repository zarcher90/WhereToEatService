"""Testing Resturant endpoints"""
import pytest

pytestmark = pytest.mark.asyncio

RESTURANTS_URL = "/v1/restaurants/"


async def test_get_restaurants(client):
    """Test the get restaurants url"""
    response = await client.get(RESTURANTS_URL)
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 1
    assert "page" in data
    assert data["page"] == 1
    assert "pages" in data
    assert data["pages"] == 1
    assert "size" in data
    assert data["size"] == 50
    assert "total" in data
    assert data["total"] == len(data["items"])


async def test_get_restaurants_contract(client):
    """Ensuring the return data is correct"""
    response = await client.get(RESTURANTS_URL)
    assert response.status_code == 200
    data = response.json()
    for restaurant in data["items"]:
        assert "uuid" in restaurant
        assert "name" in restaurant
        assert "category" in restaurant
        assert "rating" in restaurant
        assert "info" in restaurant
        assert "address" in restaurant["info"]
        assert "phoneNumber" in restaurant["info"]
        assert "openTime" in restaurant
        assert "sun" in restaurant["openTime"]
        assert "mon" in restaurant["openTime"]
        assert "tues" in restaurant["openTime"]
        assert "wed" in restaurant["openTime"]
        assert "thurs" in restaurant["openTime"]
        assert "fri" in restaurant["openTime"]
        assert "sat" in restaurant["openTime"]
        assert "diningOptions" in restaurant
        assert "dineIn" in restaurant["diningOptions"]
        assert "takeout" in restaurant["diningOptions"]
        assert "delivery" in restaurant["diningOptions"]


async def test_get_restaurants_pagination(client):
    """Testing pagination for the GET endpoint"""
    params = {"page": 1, "size": 1}
    response = await client.get(RESTURANTS_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert data["page"] == 1
    assert "pages" in data
    assert data["pages"] == 2
    assert "size" in data
    assert data["size"] == 1
    assert "total" in data
    assert data["total"] == len(data["items"]) * 2
