from typing import Optional

import fastapi
from fastapi import Depends  # Depends will get the properties from query string instead of looking in POST request

from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
	return openweather_service.get_report(loc.city, loc.state, loc.country, units)
