"""Database Module"""
import re
import logging
from fastapi import HTTPException
import motor.motor_asyncio
import pymongo
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
        Restaurants: List of restaurants in the DB. Max 1000 objects"""
    try:
        return await where_to_eat().restaurants.find().to_list(1000)
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error


async def get_restaurant_by_uuid(uuid: str):
    """Get restaurant by UUID
    Parameters:
        uuid: str
    Return:
        Restaurant: restaurant json object"""
    try:
        return await where_to_eat().restaurants.find_one({"uuid": uuid})
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error


async def get_restaurant_by_name(name: str):
    """Get restaurant by name
    Parameters:
        name: str
    Return:
        Restaurant: restaurant json object"""
    try:
        return await where_to_eat().restaurants.find_one(
            {"name": re.compile(name, re.IGNORECASE)}
        )
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error


async def add_restaurant(restaurant: dict):
    """Add restaurant to collection
    Parameters:
        restaurant: dict
    Return:
        success or fail message"""
    try:
        return await where_to_eat().restaurants.insert_one(restaurant)
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error


async def update_restaurant(restaurant_id: str, restaurant_data: dict):
    """Update restaurant
    Parameters:
        restaurant_id: str UUID of the restaurant to be updated
        restaurant_data: dict Data that is to be updated
    """
    try:
        return await where_to_eat().restaurants.update_one(
            {"uuid": restaurant_id}, {"$set": restaurant_data}
        )
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error


async def delete_restaurant(uuid: str):
    """Delete restaurant from collection
    Parameters:
        uuid: str
    """
    try:
        await where_to_eat().restaurants.delete_one({"uuid": uuid})
    except pymongo.errors.ServerSelectionTimeoutError as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail="Service is down") from error
