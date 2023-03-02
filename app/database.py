"""Database Module"""
import motor.motor_asyncio
from app.config import config

client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGODB_URL)


def where_to_eat():
    """Returns the DB connection for Where To Eat"""
    return client.where_to_eat


async def get_all_restaurants():
    """Get all restaurants
    Parameters:
        None
    Return:
        Restaurants: List of resturants in the DB. Max 1000 objects"""
    return await where_to_eat()["restaurants"].find().to_list(1000)


async def get_restaurant_by_uuid(uuid: str):
    """Get restaurant by UUID
    Parameters:
        uuid: str
    Return:
        Restaurant: restaurant json object"""
    return await where_to_eat()["restaurants"].find_one({"uuid": uuid})
