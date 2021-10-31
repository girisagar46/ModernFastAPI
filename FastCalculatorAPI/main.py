from typing import Optional

import fastapi
import uvicorn
from fastapi import FastAPI

api = FastAPI(debug=True)


@api.get("/")
def index():
	return fastapi.responses.HTMLResponse("<h1>Nice API</h1>")


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
	if z == 0:
		return fastapi.responses.JSONResponse(content={"error": "ERROR: Z is 0"}, status_code=400)
	value = (x + y)
	if z is not None:
		value /= z

	return {"value": value}


if __name__ == "__main__":
	uvicorn.run(api, host="0.0.0.0", port=8000)  # noqa
