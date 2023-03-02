"""Testing Resturant endpoints"""
import pytest

pytestmark = pytest.mark.asyncio

RESTURANTS_URL = "/v1/restaurants/"
RESTURANT_URL = "/v1/restaurant/"


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


async def test_get_restaurant(client):
    """Test getting a single resturant"""
    valid_data = {"uuid": "951d9f8e-48fa-4391-b843-16d81d7f7358", "name": "Burger Hut"}
    response = await client.get(RESTURANT_URL + valid_data["uuid"])
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert data["uuid"] == valid_data["uuid"]
    assert "name" in data
    assert data["name"] == valid_data["name"]


@pytest.mark.parametrize("invalid_url", ["123", "456"])
async def test_get_invalid_restaurant(client, invalid_url):
    """Testing geting invalid uuid"""
    response = await client.get(RESTURANT_URL + invalid_url)
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Restaurant Not Found"
