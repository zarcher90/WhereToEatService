"""Restaurants Data Model"""
from typing import Optional
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class RestaurantInfo(BaseModel):
    """Restaurant info type class"""

    address: str
    phoneNumber: str


class OpenTimes(BaseModel):
    """Opten times type class"""

    sun: str
    mon: str
    tues: str
    wed: str
    thurs: str
    fri: str
    sat: str


class DiningOptions(BaseModel):
    """Dining options type class"""

    dineIn: bool
    takeout: bool
    delivery: bool


class Restaurants(BaseModel):
    """Restaurant type class"""

    uuid: str
    name: str
    category: str
    info: RestaurantInfo = Field(...)
    openTime: OpenTimes = Field(...)
    diningOptions: DiningOptions = Field(...)
    rating: Optional[int] = None
