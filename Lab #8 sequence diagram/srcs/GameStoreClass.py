from datetime import datetime
from enum import Enum

class Customer:
	def __init__(self, name: str, age: int):
		# [C]-[Timestamp]-[Name]-[Age]
		self.__customer_id: str = f"[C]-[{datetime.now().isoformat()}]-[{name}]-[{age}]"
		self.__name: str = name
		self.__age: int = age
		self.__reservation: Reservation = None

	def get_customer_id(self):
		return self.__customer_id
	
	def get_reservation(self):
		return self.__reservation
	
	def set_reservation(self, reservation: 'Reservation'):
		self.__reservation = reservation

	reservation = property(fget=get_reservation, fset=set_reservation)
	id = property(fget=get_customer_id)

class GameStore:
	def __init__(self, store_name: str):
		# [S]-[Timestamp]-[StoreName]
		self.__store_id: str = f"[S]-[{datetime.now().isoformat()}]-[{store_name}]"
		self.__store_name: str = store_name
		self.__customer_list: list[Customer] = []
		self.__room_list: list[Room] = []
		self.__transaction_list: list[Transaction] = []
	
	def create_customer(self, name: str, age: int) -> Customer:
		new_customer = Customer(name, age)
		self.__customer_list.append(new_customer)
		return new_customer
	
	def create_room(self, max_customer: int, rate_price: float) -> 'Room':
		new_room = Room(max_customer, rate_price)
		self.__room_list.append(new_room)
		return new_room

	def get_available_room(self) -> list['Room']:
		return [room for room in self.__room_list if room.status == RoomStatusEnum.AVAILABLE]
	
	def get_all_customer(self) -> list[Customer]:
		return self.__customer_list
	
	def get_customer_by_id(self, customer_id: str) -> Customer:
		for customer in self.__customer_list:
			if customer.id == customer_id:
				return customer
		return None
	
	def get_room_by_id(self, room_id: str) -> 'Room':
		for room in self.__room_list:
			if room.id == room_id:
				return room
		return None
	
	def create_transaction(self, customer: Customer, type: 'TransactionTypeEnum') -> 'Transaction':
		new_transaction = Transaction(customer, type)
		self.__transaction_list.append(new_transaction)
		return new_transaction

	def create_booking(self, custome_id: str, room_id: str) -> str:
		customer = self.get_customer_by_id(custome_id)
		if customer is None:
			raise ValueError("Invalid User")

		room = self.get_room_by_id(room_id)
		if room is None:
			raise ValueError("No Room this ID")

		reservation = room.create_reservation(customer)
		self.create_transaction(customer, TransactionTypeEnum.RENT)
		customer.reservation = reservation
		return "Success"

class RoomStatusEnum(Enum):
	AVAILABLE = "Available"
	BEING_USE = "BeingUse"
	RESERVED = "Reserved"
	UNDER_MAINTAINACE = "UnderMaintainace"

class RoomTypeEnum(Enum):
	NORMAL = "Normal"
	VIP = "VIP"


class Room:
	def __init__(self, max_customer: int, rate_price: float):
		# [RO]-[Timestamp]-[RoomType]
		self.__room_id: str = f"[RO]-[{datetime.now().isoformat()}]-[{RoomTypeEnum.NORMAL.value}]"
		self.__max_customer: int = max_customer
		self.__rate_price: float = rate_price
		self.__room_type: RoomTypeEnum = RoomTypeEnum.NORMAL
		self.__status: RoomStatusEnum = RoomStatusEnum.AVAILABLE
		self.__reservation: Reservation = None

	def get_room_id(self) -> str:
		return self.__room_id

	id = property(fget=get_room_id)
	
	def get_status(self) -> RoomStatusEnum:
		return self.__status

	status = property(fget=get_status)

	def create_reservation(self, customer: Customer) -> 'Reservation':
		new_reservation = Reservation(customer, self)
		self.__reservation = new_reservation
		self.__status = RoomStatusEnum.RESERVED
		return new_reservation


class ReservationStatusEnum(Enum):
	PENDING = "Pending"
	SUCCESS = "Success"
	CANCEL = "CANCEL"


class Reservation:
	def __init__(self, customer: Customer, room: Room):
		# [RE]-[Timestamp]-[CustomerID]-[RoomID]
		self.__id: str = f"[RE]-[{datetime.now().isoformat()}]-[{customer.id}]-[{room.id}]"
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


class TransactionTypeEnum(Enum):
	BUY = "B"
	RENT = "R"

class TransactionStatusEnum(Enum):
	PENDING = "Pending"
	CANCEL = "Canel"
	SUCCESS = "Success"

class Transaction:
	def __init__(self, customer: Customer, type: TransactionTypeEnum):
		# [T]-[Type]-[Timestamp]-[CustomerID]
		self.__transaction_id: str = f"[T]-[{type.value}]-[{datetime.now().isoformat()}]-[{customer.id}]"
		self.__type: TransactionTypeEnum = type
		self.__customer: Customer = customer
		self.__status: TransactionStatusEnum = TransactionStatusEnum.PENDING
