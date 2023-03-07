"""Data for mock database"""
import sys
import uuid
import motor.motor_asyncio

data = [
    {
        "name": "Burger Hut",
        "uuid": "951d9f8e-48fa-4391-b843-16d81d7f7358",
        "category": "Grill",
        "info": {
            "address": "222 S Main St, Butler, PA 16001",
            "phoneNumber": "(724) 285-4222",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "7AM-8PM",
            "tues": "7AM-8PM",
            "wed": "7AM-8PM",
            "thurs": "7AM-8PM",
            "fri": "7AM-8PM",
            "sat": "7AM-8PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 5,
    },
    {
        "name": "Rachel's Roadhouse",
        "uuid": "ddaaa1b4-cd34-444f-ae8e-0b4c0561f733",
        "category": "American",
        "info": {
            "address": "100 Fairfield Ln, Butler, PA 16001",
            "phoneNumber": "(724) 841-0333",
        },
        "openTime": {
            "sun": "12-9PM",
            "mon": "11AM-9PM",
            "tues": "11AM-9PM",
            "wed": "11AM-9PM",
            "thurs": "11AM-9PM",
            "fri": "11AM-10PM",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 4,
    },
    {
        "name": "Anna Maria's Pizza",
        "category": "Pizza",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "113 Freeport Rd, Butler, PA 16002",
            "phoneNumber": "(724) 431-2233",
        },
        "openTime": {
            "sun": "3PM-8PM",
            "mon": "Closed",
            "tues": "Closed",
            "wed": "Closed",
            "thurs": "11AM-9PM",
            "fri": "11AM-9PM",
            "sat": "11AM-9PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": True},
        "rating": 0,
    },
    {
        "name": "Cannella Cafe",
        "category": "Cafe",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "232 S Main St, Butler, PA 16001",
            "phoneNumber": "(724) 256-5111",
        },
        "openTime": {
            "sun": "7AM-2PM",
            "mon": "7AM-2PM",
            "tues": "7AM-2PM",
            "wed": "7AM-2PM",
            "thurs": "7AM-2PM",
            "fri": "7AM-2PM",
            "sat": "7AM-2PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 0,
    },
    {
        "name": "Mac's Route 8 Cafe",
        "category": "Cafe",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "16 Pittsburgh Rd, Butler, PA 16001",
            "phoneNumber": "(724) 256-9710",
        },
        "openTime": {
            "sun": "7AM-2PM",
            "mon": "7AM-2PM",
            "tues": "7AM-2PM",
            "wed": "7AM-2PM",
            "thurs": "7AM-2PM",
            "fri": "7AM-2PM",
            "sat": "7AM-2PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 0,
    },
    {
        "name": "Chop Shop",
        "category": "American",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "108 N Main St, Butler, PA 16001",
            "phoneNumber": "(724) 256-9959",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "Closed",
            "tues": "11AM-9PM",
            "wed": "11AM-9PM",
            "thurs": "11AM-9PM",
            "fri": "11AM-10PM",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 0,
    },
    {
        "name": "Mama Rosa's Restaurant",
        "category": "Itailian",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "263 Old Plank Rd, Butler, PA 16002",
            "phoneNumber": "(724) 287-7315",
        },
        "openTime": {
            "sun": "11AM-8PM",
            "mon": "Closed",
            "tues": "11AM-9PM",
            "wed": "11AM-9PM",
            "thurs": "11AM-9PM",
            "fri": "11AM-10PM",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": False},
        "rating": 0,
    },
    {
        "name": "Natili North",
        "category": "Italian",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "204 N Main St, Butler, PA 16001",
            "phoneNumber": "(724) 283-2149",
        },
        "openTime": {
            "sun": "Closed",
            "mon": "11AM-8PM",
            "tues": "11AM-8PM",
            "wed": "11AM-8PM",
            "thurs": "11AM-8PM",
            "fri": "11AM-9PM",
            "sat": "3PM-9PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": True},
        "rating": 0,
    },
    {
        "name": "Rey Azteca Butler",
        "category": "Mexican",
        "uuid": str(uuid.uuid4()),
        "info": {
            "address": "138 Point Plaza, Butler, PA 16001",
            "phoneNumber": "(724) 285-2600",
        },
        "openTime": {
            "sun": "12PM-8PM",
            "mon": "11AM-9PM",
            "tues": "11AM-9PM",
            "wed": "11AM-9PM",
            "thurs": "11AM-9PM",
            "fri": "11AM-10PM",
            "sat": "11AM-10PM",
        },
        "diningOptions": {"dineIn": True, "takeout": True, "delivery": True},
        "rating": 0,
    },
]


def load_data(db_url: str):
    """Loads a database with the initial data
    Parameters:
        db_url: str Database connection url"""
    client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
    client.where_to_eat.restaurants.insert_many(data)


if __name__ == "__main__":
    globals()[sys.argv[1]](sys.argv[2])
