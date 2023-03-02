"""Resturants Router"""
from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
import app.database as db
from app.v1.models.restaurants import Restaurants

router = APIRouter()


@router.get("/restaurants/", response_model=Page[Restaurants])
async def get_restaurants():
    """GET all restaurants"""
    return paginate(await db.get_all_restaurants())


@router.get("/restaurant/{restaurant_id}", response_model=Restaurants)
async def get_restaurant(restaurant_id):
    """GET a restaurant"""
    if (restaurant := await db.get_restaurant_by_uuid(restaurant_id)) is not None:
        return restaurant
    raise HTTPException(status_code=404, detail="Restaurant Not Found")


add_pagination(router)
