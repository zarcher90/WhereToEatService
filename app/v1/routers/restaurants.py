"""Resturants Router"""
from fastapi import APIRouter
from fastapi_pagination import Page, add_pagination, paginate
import app.database as db
from app.v1.models.restaurants import Restaurants

router = APIRouter()


@router.get("/restaurants/", response_model=Page[Restaurants])
async def get_restaurants():
    """GET all restaurants"""
    return paginate(await db.get_all_restaurants())


add_pagination(router)
