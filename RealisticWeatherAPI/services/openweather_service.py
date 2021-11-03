from typing import Optional

import httpx
from decouple import config

from infrastructure import weather_cache
from models.validation import ValidationError

api_key: str = config("OPEN_WEATHER_API")


async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
	if forecast := weather_cache.get_weather(city, state, country, units):
		return forecast

	q = f'{city},{state},{country}' if state else f'{city},{country}'
	url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
	async with httpx.AsyncClient() as client:
		resp: httpx.Response = await client.get(url)
		if resp.is_client_error:
			raise ValidationError(resp.text, status_code=resp.status_code)
		resp.raise_for_status()

	data = resp.json()
	weather_cache.set_weather(city, state, country, units, forecast)
	return data["main"]
