from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from GameStoreClass import GameStore, Customer, Reservation
import uvicorn

app = FastAPI()

store = GameStore("GameStore Demo")

@app.get("/")
def test_connection():
	return "Hello World"

@app.post("/create_customer")
def create_customer(name: str, age: int):
	return store.create_customer(name, age).id

@app.get("/get_all_customer")
def	get_all_customer():
	return [customer.id for customer in store.get_all_customer()]

@app.post("/create_room")
def create_room(max_customer: int, rate_price: float):
	return store.create_room(max_customer, rate_price).id

@app.get("/available_room")
def get_available_room():
	return [room.id for room in store.get_available_room()]

@app.post("/booking")
def booking(customer_id: str, room_id: str):
	try:
		return store.create_booking(customer_id, room_id)
	except Exception as e:
		return {e.__str__()}

@app.get("/check_reservation")
def check_reservation(customer_id: str):
	customer: Customer = store.get_customer_by_id(customer_id)
	reservation: Reservation = customer.reservation
	return reservation.id

if __name__ == "__main__":
	uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)