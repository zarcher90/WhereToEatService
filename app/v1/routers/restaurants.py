"""Resturants Router"""
from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
import app.database as db
from app.v1.models.restaurants import Restaurants, UpdateRestaurants

router = APIRouter()


async def is_restaurant_duplicate(restaurant: Restaurants):
    """Checks to see if restaurant is a duplicate value based on name and uuid
    Parameters:
        restaurant: Restaurants
    Return:
        boolean: True or False to indicate duplicate or not"""
    if await db.get_restaurant_by_name(restaurant.name) is not None:
        return True
    if await db.get_restaurant_by_uuid(restaurant.uuid) is not None:
        return True

    return False


async def does_restaurant_exist(restaurant_id: str):
    """Checks to see if restaurant exist in db based on uuid
    Parameters:
        restaurant_id: str
    Return:
        boolean: True or False to indicate existing object"""
    if await db.get_restaurant_by_uuid(restaurant_id) is not None:
        return True

    return False


@router.get("/restaurants", response_model=Page[Restaurants])
async def get_restaurants():
    """GET all restaurants"""
    return paginate(await db.get_all_restaurants())


@router.get("/restaurants/{restaurant_id}", response_model=Restaurants)
async def get_restaurant(restaurant_id):
    """GET a restaurant"""
    if (restaurant := await db.get_restaurant_by_uuid(restaurant_id)) is not None:
        return restaurant
    raise HTTPException(status_code=404, detail="Restaurant Not Found")


@router.post("/restaurants", response_model=Restaurants)
async def add_restaurant(restaurant: Restaurants):
    """Add a restaurant"""
    if not await is_restaurant_duplicate(restaurant):
        await db.add_restaurant(restaurant.dict())
        return restaurant
    raise HTTPException(status_code=400, detail="Restaurant Not Added")


@router.put("/restaurants/{restaurant_id}", response_model=Restaurants)
async def update_restaurant(restaurant_id: str, restaurant: UpdateRestaurants):
    """Update restaurant"""
    if await does_restaurant_exist(restaurant_id):
        await db.update_restaurant(restaurant_id, restaurant.dict())
        return await db.get_restaurant_by_uuid(restaurant_id)
    raise HTTPException(status_code=404, detail="Restaurant Not Found")


@router.delete("/restaurants/{restaurant_id}")
async def delete_restaurant(restaurant_id: str):
    """Delete a restaurant"""
    if await does_restaurant_exist(restaurant_id):
        await db.delete_restaurant(restaurant_id)
        return {"message": "Successful"}
    raise HTTPException(status_code=400, detail="There was an error")


add_pagination(router)
