from typing import Optional, List

import fastapi
from fastapi import Depends  # Depends will get the properties from query string instead of looking in POST request

from models.location import Location
from models.report import Report, ReportSubmittal
from models.validation import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
	try:
		return await openweather_service.get_report(loc.city, loc.state, loc.country, units)
	except ValidationError as ve:
		return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)


@router.get("/api/reports", name="all_reports")
async def reports_get() -> List[Report]:
	return await report_service.get_reports()


@router.post("/api/reports", name="add_reports", status_code=201)
async def reports_post(report_submitted: ReportSubmittal) -> Report:
	d = report_submitted.description
	loc = report_submitted.location
	return await report_service.add_report(d, loc)
