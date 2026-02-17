from __future__ import annotations

from enum import Enum
import uuid


def make_id(prefix: str) -> str:
	# Example: C-550e8400-e29b-41d4-a716-446655440000
	return f"{prefix}-{uuid.uuid4()}"


class Customer:
	def __init__(self, customer_id: str, name: str, age: int):
		self.__customer_id: str = customer_id
		self.__name: str = name
		self.__age: int = age
		self.__reservation: Reservation | None = None

	def get_customer_id(self):
		return self.__customer_id

	def get_reservation(self):
		return self.__reservation

	def set_reservation(self, reservation: "Reservation"):
		self.__reservation = reservation

	reservation = property(fget=get_reservation, fset=set_reservation)
	id = property(fget=get_customer_id)


class RoomStatusEnum(Enum):
	AVAILABLE = "Available"
	BEING_USE = "BeingUse"
	RESERVED = "Reserved"
	UNDER_MAINTAINACE = "UnderMaintainace"


class RoomTypeEnum(Enum):
	NORMAL = "Normal"
	VIP = "VIP"


class Room:
	def __init__(self, room_id: str, max_customer: int, rate_price: float):
		self.__room_id: str = room_id
		self.__max_customer: int = max_customer
		self.__rate_price: float = rate_price
		self.__room_type: RoomTypeEnum = RoomTypeEnum.NORMAL
		self.__status: RoomStatusEnum = RoomStatusEnum.AVAILABLE
		self.__reservation: Reservation | None = None

	def get_room_id(self) -> str:
		return self.__room_id

	id = property(fget=get_room_id)

	def get_status(self) -> RoomStatusEnum:
		return self.__status

	status = property(fget=get_status)

	def create_reservation(self, reservation_id: str, customer: Customer) -> "Reservation":
		new_reservation = Reservation(reservation_id, customer, self)
		self.__reservation = new_reservation
		self.__status = RoomStatusEnum.RESERVED
		return new_reservation


class ReservationStatusEnum(Enum):
	PENDING = "Pending"
	SUCCESS = "Success"
	CANCEL = "CANCEL"


class Reservation:
	def __init__(self, reservation_id: str, customer: Customer, room: Room):
		self.__id: str = reservation_id
		self.__customer: Customer = customer
		self.__room: Room = room
		self.__status: ReservationStatusEnum = ReservationStatusEnum.PENDING

	def get_status(self):
		return self.__status

	def set_status(self, status: ReservationStatusEnum):
		self.__status = status

	status = property(fget=get_status, fset=set_status)

	def get_id(self):
		return self.__id

	id = property(fget=get_id)

class Logs:
	def __init__(self, transaction_id: str):
		self.__transaction_id: str = transaction_id

class CustomerAction(Enum):
	CREATE_RESERVATION = "Create Reservation"

class CustomerLogs(Logs):
	def __init__(self, transaction_id: str, customer: Customer, action: CustomerAction):
		super().__init__(transaction_id)
		self.__customer: Customer = customer
		self.__action: CustomerAction = action

class GameStore:
	def __init__(self, store_name: str):
		self.__store_id: str = make_id("S")
		self.__store_name: str = store_name
		self.__customer_list: list[Customer] = []
		self.__room_list: list[Room] = []
		self.__customer_logs_list: list[Transaction] = []

	def create_customer(self, name: str, age: int) -> Customer:
		new_customer = Customer(make_id("C"), name, age)
		self.__customer_list.append(new_customer)
		return new_customer

	def create_room(self, max_customer: int, rate_price: float) -> Room:
		new_room = Room(make_id("RO"), max_customer, rate_price)
		self.__room_list.append(new_room)
		return new_room

	def get_available_room(self) -> list[Room]:
		return [room for room in self.__room_list if room.status == RoomStatusEnum.AVAILABLE]

	def get_all_customer(self) -> list[Customer]:
		return self.__customer_list

	def get_customer_by_id(self, customer_id: str) -> Customer | None:
		for customer in self.__customer_list:
			if customer.id == customer_id:
				return customer
		return None

	def get_room_by_id(self, room_id: str) -> Room | None:
		for room in self.__room_list:
			if room.id == room_id:
				return room
		return None

	def create_customer_logs(self, customer: Customer, action: CustomerAction) -> Transaction:
		new_log = CustomerLogs(make_id(f"LC-{action}"), customer, action)
		self.__customer_list.append(new_log)
		return new_log

	def create_booking(self, customer_id: str, room_id: str) -> str:
		customer = self.get_customer_by_id(customer_id)
		if customer is None:
			raise ValueError("Invalid User")

		room = self.get_room_by_id(room_id)
		if room is None:
			raise ValueError("No Room this ID")

		reservation = room.create_reservation(make_id("RE"), customer)
		self.create_customer_logs(customer, CustomerAction.CREATE_RESERVATION)
		customer.reservation = reservation
		return "Success"
