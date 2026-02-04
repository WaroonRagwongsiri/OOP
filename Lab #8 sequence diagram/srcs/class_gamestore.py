from enum import Enum

class Customer:
	def __init__(self, customer_id: str, name: str, age: int):
		self.__customer_id: str = customer_id
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
	def __init__(self, store_id: str, store_name: str):
		self.__store_id: str = store_id
		self.__store_name: str = store_name
		self.__customer_list: list[Customer] = []
		self.__room_list: list[Room] = []
		self.__transaction_list: list[Transaction] = []
	
	def create_customer(self, customer_id:str, name: str, age: int) -> Customer:
		new_customer: Customer = Customer(customer_id, name, age)
		self.__customer_list.append(new_customer)
		return new_customer
	
	def create_room(self, room_id: str, max_customer: int, rate_price: float) -> 'Room':
		new_room = Room(room_id, max_customer, rate_price)
		self.__room_list.append(new_room)
		return new_room

	def get_available_room(self) -> list['Room']:
		available_rooms = []

		for room in self.__room_list:
			if room.status == RoomStatusEnum.AVAILABLE:
				available_rooms.append(room)
		
		return available_rooms
	
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
	
	def create_transaction(self, transaction_id:str, customer: Customer, type: int) -> 'Transaction':
		new_transaction = Transaction(transaction_id, customer, type)
		self.__transaction_list.append(new_transaction)
		return new_transaction

	def create_booking(self, custome_id: str, room_id: str) -> str:
		customer = self.get_customer_by_id(custome_id)
		if customer == None:
			raise ValueError("Invalid User")
		room = self.get_room_by_id(room_id)
		if room == None:
			raise ValueError("No Room this ID")
		reservation = room.create_reservation('Reservation-OK', customer)
		if reservation == None:
			raise ValueError("Fail to create Reservation")
		self.create_transaction('RE-00', customer, TransactionTypeEnum.RENT)
		customer.reservation = reservation
		return "Success"

class RoomStatusEnum(Enum):
	AVAILABLE = 0
	BEING_USE = 1
	UNDER_MAINTAINACE = 2

class Room:
	def __init__(self, room_id: str, max_customer: int, rate_price: float):
		self.__room_id: str = room_id
		self.__max_customer: int = max_customer
		self.__rate_price: float = rate_price
		self.__status: RoomStatusEnum = RoomStatusEnum.AVAILABLE
		self.__reservation: list[Reservation] = []

	def get_room_id(self) -> str:
		return self.__room_id

	id = property(fget=get_room_id)
	
	def get_status(self) -> int:
		return self.__status

	status = property(fget=get_status)

	def create_reservation(self, reservation_id: str, customer: Customer) -> 'Reservation':
		new_reservation = Reservation(reservation_id, customer, self)
		self.__reservation.append(new_reservation)
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
		self.__status: int = ReservationStatusEnum.PENDING

	def get_status(self):
		return self.__status
	
	def set_status(self, status: ReservationStatusEnum):
		self.__status = status

	status = property(fget=get_status, fset=set_status)

	def get_id(self):
		return self.__id
	
	id = property(fget=get_id)

class TransactionTypeEnum(Enum):
	BUY = 0
	RENT = 1

class TransactionStatusEnum(Enum):
	PENDING = 0
	CANCEL = 1
	SUCCESS = 2

class Transaction:
	def __init__(self, transaction_id: str, customer: Customer, type: TransactionStatusEnum):
		self.__transaction_id: str = transaction_id
		self.__type: TransactionStatusEnum = type
		self.__customer: Customer = customer
		self.__status: TransactionStatusEnum = TransactionStatusEnum.PENDING