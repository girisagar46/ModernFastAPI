import datetime
from typing import Optional, List

from pydantic import BaseModel

external_data = {
	"item_id": "124",
	"created_date": "2021-11-24 12:22",
	"pages_visited": [1, 2, "3"],
	"price": 100.4
}


class Order(BaseModel):
	item_id: int
	created_date: Optional[datetime.datetime]  # this can be omitted in external data
	pages_visited: List[int]
	price: float


if __name__ == '__main__':
	o = Order(**external_data)
	print(o)
