from typing import Optional

import fastapi
from fastapi import Depends  # Depends will get the properties from query string instead of looking in POST request

from models.location import Location
from models.validation import ValidationError
from services import openweather_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
	try:
		return await openweather_service.get_report(loc.city, loc.state, loc.country, units)
	except ValidationError as ve:
		return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
