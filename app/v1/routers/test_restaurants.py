"""Testing Resturant endpoints"""
import uuid
import pytest

pytestmark = pytest.mark.asyncio

RESTURANTS_URL = "/v1/restaurants"
RESTURANT_URL = "/v1/restaurant"


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


async def test_get_restaurant(client, valid_data):
    """Test getting a single resturant"""
    response = await client.get(f"{RESTURANT_URL}/{valid_data['uuid']}")
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert data["uuid"] == valid_data["uuid"]
    assert "name" in data
    assert data["name"] == valid_data["name"]


@pytest.mark.parametrize("invalid_url", ["123", "456"])
async def test_get_invalid_restaurant(client, invalid_url):
    """Testing geting invalid uuid"""
    response = await client.get(f"{RESTURANT_URL}/{invalid_url}")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Restaurant Not Found"


async def test_create_restaurant(client):
    """Test creating a restaurant"""
    payload = {
        "name": "Zachs's Roadhouse",
        "category": "American",
        "info": {
            "address": "109 Dolphin DR, Butler, PA 16002",
            "phoneNumber": "(724) 822-8044",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "Closed",
            "tues": "Closed",
            "wed": "Closed",
            "thurs": "Closed",
            "fri": "Closed",
            "sat": "Closed",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 2,
    }
    response = await client.post(RESTURANT_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert data["name"] == payload["name"]
    assert data["category"] == payload["category"]
    assert data["info"] == payload["info"]
    assert data["openTime"] == payload["openTime"]
    assert data["diningOptions"] == payload["diningOptions"]
    assert data["rating"] == payload["rating"]


async def test_create_restaurant_with_uuid(client):
    """Test creating a restaurant with uuid"""
    payload = {
        "name": "Zachs's Bar",
        "uuid": str(uuid.uuid4()),
        "category": "Grill",
        "info": {
            "address": "104 Dolphin DR, Butler, PA 16002",
            "phoneNumber": "(724) 822-8044",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "11AM-10PM",
            "tues": "11AM-10PM",
            "wed": "11AM-10PM",
            "thurs": "11AM-10PM",
            "fri": "11AM-2PM",
            "sat": "11AM-12PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 2,
    }
    response = await client.post(RESTURANT_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["uuid"] == payload["uuid"]
    assert data["name"] == payload["name"]
    assert data["category"] == payload["category"]
    assert data["info"] == payload["info"]
    assert data["openTime"] == payload["openTime"]
    assert data["diningOptions"] == payload["diningOptions"]
    assert data["rating"] == payload["rating"]


async def test_create_duplicate_restaurant(client):
    """Test creating a duplicate restaurant"""
    payload = {
        "name": "Rachel's Roadhouse",
        "category": "American",
        "info": {
            "address": "987 Fairfield Ln, Butler, PA 16001",
            "phoneNumber": "(724) 841-0674",
        },
        "openTime": {
            "sun": "12-11PM",
            "mon": "11AM-11PM",
            "tues": "11AM-11PM",
            "wed": "11AM-11PM",
            "thurs": "11AM-11PM",
            "fri": "11AM-11PM",
            "sat": "11AM-11PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 4,
    }
    response = await client.post(RESTURANT_URL, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Restaurant Not Added"


async def test_create_duplicate_uuid(client):
    """Test creating a duplicate uuid"""
    payload = {
        "name": "Rach house",
        "uuid": "ddaaa1b4-cd34-444f-ae8e-0b4c0561f733",
        "category": "American",
        "info": {
            "address": "1000 Fairfield Ln, Butler, PA 16001",
            "phoneNumber": "(724) 841-9876",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "10AM-9PM",
            "tues": "10AM-9PM",
            "wed": "10AM-9PM",
            "thurs": "11AM-9PM",
            "fri": "Closed",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 4,
    }
    response = await client.post(RESTURANT_URL, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Restaurant Not Added"


async def test_create_with_missing_data(client):
    """Test creating with missing data"""
    payload = {
        "name": "Rach house",
        "uuid": "ddaaa1b4-cd34-444f-ae8e-0b4c0561f733",
        "category": "American",
        "info": {
            "address": "800 Faird Ln, Butler, PA 16001",
            "phoneNumber": "(724) 841-0934",
        },
    }
    response = await client.post(RESTURANT_URL, json=payload)
    assert response.status_code == 422


async def test_delete_restaurant(client, valid_data):
    """Test deletion of a restaurant"""
    response = await client.delete(f"{RESTURANT_URL}/{valid_data['uuid']}")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Successful"}


async def test_delete_invalid_resaurant(client):
    """Test deletion of a restaurant that does not exist"""
    response = await client.delete(RESTURANT_URL + "/123")
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "There was an error"
