"""Restaurants Data Model"""
import uuid
from typing import Optional
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class RestaurantInfo(BaseModel):  # pylint: disable=too-few-public-methods
    """Restaurant info type class"""

    address: str
    phoneNumber: str


class OpenTimes(BaseModel):  # pylint: disable=too-few-public-methods
    """Opten times type class"""

    sun: str
    mon: str
    tues: str
    wed: str
    thurs: str
    fri: str
    sat: str


class DiningOptions(BaseModel):  # pylint: disable=too-few-public-methods
    """Dining options type class"""

    dineIn: bool
    takeout: bool
    delivery: bool


class Restaurants(BaseModel):  # pylint: disable=too-few-public-methods
    """Restaurant type class"""

    uuid: str = str(uuid.uuid4())
    name: str
    category: str
    info: RestaurantInfo = Field(...)
    openTime: OpenTimes = Field(...)
    diningOptions: DiningOptions = Field(...)
    rating: Optional[int] = None
