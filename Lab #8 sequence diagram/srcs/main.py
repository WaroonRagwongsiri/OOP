from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from class_gamestore import GameStore

import uvicorn

app = FastAPI()

store = GameStore("S001", "GameStore Demo")

customer = store.create_customer("C-0", "TestCustomer", 20)
room = store.create_room("R-0", 10, 12)

@app.get("/")
def test_connection():
	return "Hello World"

@app.get("/available_room")
def get_available_room():
	return store.get_available_room()

@app.post("/booking")
def booking(room_id: str):
	try:
		return store.create_booking(customer.id, room_id)
	except Exception as e:
		return {e.__str__()}

@app.get("/check_reservation")
def check_reservation():
	return customer.reservation.status

if __name__ == "__main__":
	uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)