from typing import List, Union, Optional

##################################################################################
# Instruction for Students:
# 1. จงเขียน Class Diagram เพื่อออกแบบ Class ต่างๆ ให้รองรับการทำงานของ Code ส่วนล่าง
# 2. จงเขียน Class Definition (Bank, User, Account, ATM_Card, ATM_machine, Transaction)
#    เพื่อให้สามารถรัน Function run_test() ได้โดยไม่เกิด Error
# 3. ห้ามแก้ไข Code ในส่วนของ create_bank_system() และ run_test() โดยเด็ดขาด
# 4. ต้องมีการ Validate ข้อมูลตามเงื่อนไขที่กำหนดในเอกสาร Lab (เช่น เงินไม่พอ, PIN ผิด)
#    และทำการ Raise Exception เมื่อเกิดข้อผิดพลาด
##################################################################################

# --- พื้นที่สำหรับเขียน Class ของนักศึกษา (เขียนต่อจากตรงนี้) ---

class Bank:
	def __init__(self, bank_name: str):
		self.__bank_name: str = bank_name
		self.__user_list: list[User] = list()
		self.__atm_list: list[ATM_machine] = list()

	def add_user(self, user: 'User'):
		if not isinstance(user, User):
			raise TypeError
		self.__user_list.append(user)
	
	def add_atm_machine(self, atm: 'ATM_machine'):
		if not isinstance(atm, ATM_machine):
			raise TypeError
		self.__atm_list.append(atm)
		atm.bank = self
	
	def get_atm_by_id(self, id: str) -> 'ATM_machine':
		if not isinstance(id, str):
			raise TypeError
		for index, item in enumerate(self.__atm_list):
			atm: ATM_machine = item
			if atm.atm_id == id:
				return atm
		return None
	
	def search_account_from_atm(self, id: str) -> 'Account':
		if not isinstance(id, str):
			raise TypeError
		for index1, item1 in enumerate(self.__atm_list):
			atm: ATM_machine = item1
			bank: Bank = atm.bank
			all_user : list[User] = bank.user_list
			for index2, item2 in enumerate(bank.user_list):
				user: User = item2
				for index3, item3 in enumerate(user.acc_list):
					acc: Account = item3
					atm_card: ATM_Card = acc.atm_card
					if atm_card.atm_card_id == id:
						return acc
		return None

	def validate_card(self, atm_card: 'ATM_Card', pin: str) -> bool:
		if not isinstance(atm_card, ATM_Card) or not isinstance(pin, str):
			raise TypeError
		for index1, item1 in enumerate(self.__user_list):
			user: User = item1
			for index2, item2 in enumerate(user.acc_list):
				acc: Account = item2
				acc_atm_card: ATM_Card = acc.atm_card
				if acc_atm_card == atm_card:
					return acc_atm_card.is_correct_pin(pin)
		return False
	
	def get_user_list(self):
		return self.__user_list
	
	user_list = property(fget=get_user_list)

class User:
	def __init__(self, user_id: str, name: str):
		self.__user_id: str = user_id
		self.__name: str = name
		self.__acc_list: list[Account] = list()
	
	def add_account(self, account: 'Account'):
		if not isinstance(account, Account):
			raise TypeError
		self.__acc_list.append(account)
	
	def get_acc_list(self) -> list['Account']:
		return self.__acc_list
	
	acc_list = property(fget=get_acc_list)

class Account:
	daily_limit = 40000
	fees = 150

	def __init__(self, acc_id: str, user: User, balance: float):
		self.__acc_id: str = acc_id
		self.__user: User = user
		self.__balance: float = balance
		self.__atm_card: ATM_Card = None
		self.__transaction_list: list[Transaction] = list()
	
	def get_acc_id(self) -> str:
		return self.__acc_id
	
	def get_atm_card(self) -> 'ATM_Card':
		return self.__atm_card

	def add_atm_card(self, atm_card: 'ATM_Card'):
		if not isinstance(atm_card, ATM_Card):
			raise TypeError
		self.__atm_card = atm_card

	def get_balance(self) -> float:
		return self.__balance
	
	def add_transaction(self, transaction: 'Transaction'):
		if not isinstance(transaction, Transaction):
			raise TypeError
		self.__transaction_list.append(transaction)

	def deposit(self, atm: 'ATM_machine', amount):
		if not isinstance(atm, ATM_machine) or (not isinstance(amount, float) and not isinstance(amount, int)):
			raise TypeError("Atm or Amount is wrong type")
		if not atm.validate_holder(self.account_no):
			raise ValueError("Wrong account")
		if amount < 0:
			raise ValueError("Amount less than 0")
		self.__balance += amount
		transaction = Transaction('D', atm.atm_id, amount, self.__balance, None)
		self.add_transaction(transaction)

	def withdraw(self, atm: 'ATM_machine', amount):
		if not isinstance(atm, ATM_machine) or (not isinstance(amount, float) and not isinstance(amount, int)):
			raise TypeError("Atm or Amount is wrong type")
		if not atm.validate_holder(self.account_no):
			raise ValueError("Wrong account")
		if amount < 0 or amount > self.__balance or amount > self.daily_limit:
			raise ValueError("Amount less than 0 or Amount exceed daily limit")
		self.__balance -= amount
		self.daily_limit -= amount
		transaction = Transaction('W', atm.atm_id, amount, self.__balance, None)
		self.add_transaction(transaction)

	def transfer(self, atm: 'ATM_machine', amount, target: 'Account'):
		if not isinstance(atm, ATM_machine) or (not isinstance(amount, float) and not isinstance(amount, int)) or not isinstance(target, Account):
			raise TypeError("Atm or Amount or Target is wrong type")
		if not atm.validate_holder(self.account_no):
			raise ValueError("Wrong account")
		if amount < 0 or amount > self.__balance or amount > self.daily_limit:
			raise ValueError("Amount less than 0 or Amount exceed daily limit")
		self.__balance -= amount
		target.amount += amount
		me_transaction = Transaction('TD', atm.atm_id, amount, self.__balance, target.account_no)
		target_transaction = Transaction('TW', atm.atm_id, amount, target.amount, self.account_no)
		self.add_transaction(me_transaction)
		target.add_transaction(target_transaction)

	def print_transactions(self):
		for index, item in enumerate(self.__transaction_list):
			print(index, item)

	def annual_fees_cut(self):
		if self.__balance - self.fees < 0:
			raise ValueError("Account balance is less than annual fee")
	
	def reset_annual_limit(self):
		self.daily_limit = 40000

	account_no = property(fget=get_acc_id)
	atm_card = property(fget=get_atm_card, fset=add_atm_card)
	amount = property(fget=get_balance)

class ATM_Card:
	def __init__(self, atm_card_id: str, acc_id: str, pin: str):
		self.__atm_card_id: str = atm_card_id
		self.__acc_id: str = acc_id
		self.__pin: str = pin
	
	def is_correct_pin(self, pin: str) -> bool:
		if not isinstance(pin, str):
			raise TypeError
		return self.__pin == pin
	
	def get_atm_card_id(self):
		return self.__atm_card_id
	
	def get_acc_id(self):
		return self.__acc_id

	atm_card_id = property(fget=get_atm_card_id)
	acc_id = property(fget=get_acc_id)

class ATM_machine:
	def __init__(self, atm_id: str, money: float):
		self.__atm_id: str = atm_id
		self.__money: str = money
		self.__bank: Bank = None
		self.__card_holder_id: str = None

	def get_id(self) -> str:
		return self.__atm_id

	def insert_card(self, atm_card: 'ATM_Card', pin: str) -> bool:
		if not isinstance(atm_card, ATM_Card):
			raise TypeError
		is_correct_card = self.__bank.validate_card(atm_card, pin)
		if is_correct_card:
			self.__card_holder_id = atm_card.acc_id
		return is_correct_card

	def validate_holder(self, acc_id: str) -> bool:
		return self.__card_holder_id == acc_id

	def set_bank(self, bank: Bank):
		if not isinstance(bank, Bank):
			raise TypeError
		self.__bank = bank
	
	def get_bank(self):
		return self.__bank

	atm_id = property(fget=get_id)
	bank = property(fget=get_bank, fset=set_bank)

class Transaction:
	def __init__(self, type: str, atm_id: str, amount: float, balance: float, target_acc_id: str = None):
		self.__type: str = type
		self.__atm_id: str = atm_id
		self.__amount: float = amount
		self.__balance: float = balance
		self.__target_acc_id: str = target_acc_id


##################################################################################
# Test Case & Setup : ห้ามแก้ไข Code ส่วนนี้
# ใช้สำหรับตรวจสอบว่า Class ที่ออกแบบมาถูกต้องตาม Requirement หรือไม่
##################################################################################

def create_bank_system() -> Bank:
	print("--- Setting up Bank System ---")
	
	# 1. กำหนดชื่อธนาคาร
	scb = Bank("SCB")
	
	# 2. สร้าง User, Account, ATM_Card
	# Data format: CitizenID: [Name, AccountNo, ATM Card No, Balance]
	user_data = {
	'1-1101-12345-12-0': ['Harry Potter', '1000000001', '12345', 20000],
	'1-1101-12345-13-0': ['Hermione Jean Granger', '1000000002', '12346', 1000]
	}
	
	for citizen_id, detail in user_data.items():
		name, account_no, atm_no, amount = detail
		
		user_instance = User(citizen_id, name)
		user_account = Account(account_no, user_instance, amount)
		atm_card = ATM_Card(atm_no, account_no, '1234')
		
		user_account.add_atm_card(atm_card)
		user_instance.add_account(user_account)
		scb.add_user(user_instance)

	# 3. สร้างตู้ ATM
	scb.add_atm_machine(ATM_machine('1001', 1000000))
	scb.add_atm_machine(ATM_machine('1002', 200000))

	return scb

def run_test():
	scb = create_bank_system()
	
	atm_machine1 = scb.get_atm_by_id('1001')
	atm_machine2 = scb.get_atm_by_id('1002')
	
	harry_account = scb.search_account_from_atm('12345')
	hermione_account = scb.search_account_from_atm('12346')
	
	# ตรวจสอบว่าหา Account เจอหรือไม่
	if not harry_account or not hermione_account:
		print("Error: Could not find accounts. Check your search_account_from_atm method.")
		return

	harry_card = harry_account.atm_card
	hermione_card = hermione_account.atm_card
	
	print("\n--- Test Case #1 : Insert Card (Harry) ---")
	print(f"Harry's Account No : {harry_account.account_no}")

	if atm_machine2.insert_card(hermione_card, "1234"):
		print("Success: ATM accepted valid card and PIN")
	else:
		print("Error: ATM rejected valid card")

	print("\n--- Test Case #2 : Deposit 1000 to Hermione ---")
	print(f"Before: {hermione_account.amount}")

	try:
		hermione_account.deposit(atm_machine2, 1000)
		print(f"After: {hermione_account.amount}")
	except Exception as e:
		print(f"Error: {e}")

	print("\n--- Test Case #3 : Deposit -1 (Expect Error) ---")
	try:
		hermione_account.deposit(atm_machine2, -1)
		print("Error: Failed to catch negative deposit")
	except ValueError as e: # คาดหวัง ValueError หรือ Exception ที่เหมาะสม
		print(f"Pass: System correctly raised error -> {e}")
	except Exception as e:
		print(f"Pass: System raised error -> {e}")

	print("\n--- Test Case #4 : Withdraw 500 from Hermione ---")
	print(f"Before: {hermione_account.amount}")

	try:
		hermione_account.withdraw(None, 500)
		print(f"After: {hermione_account.amount}")
	except Exception as e:
		print(f"Error: {e}")

	print("\n--- Test Case #5 : Withdraw Excess Balance (Expect Error) ---")
	try:
		hermione_account.withdraw(atm_machine2, 30000)
		print("Error: Failed to catch overdraft")
	except Exception as e:
		print(f"Pass: System correctly raised error -> {e}")

	print("\n--- Test Case #6 : Transfer 10000 from Harry to Hermione ---")
	print(f"Harry Before: {harry_account.amount}")
	print(f"Hermione Before: {hermione_account.amount}")

	try:
		harry_account.transfer(atm_machine2, 10000, hermione_account)
		print(f"Harry After: {harry_account.amount}")
		print(f"Hermione After: {hermione_account.amount}")
	except Exception as e:
		print(f"Error: {e}")

	print("\n--- Test Case #7 : Transaction History ---")

	print("Harry Transactions:")
	harry_account.print_transactions()
	print("Hermione Transactions:")
	hermione_account.print_transactions()

	print("\n--- Test Case #8 : Wrong PIN (Expect Error) ---")
	if not atm_machine1.insert_card(harry_card, "1234"):
		print("Pass: ATM correctly rejected wrong PIN")
	else:
		print("Error: ATM accepted wrong PIN")
		
	print("\n--- Test Case #9 : Exceed Daily Limit (Expect Error) ---")
	# Harry ถอนไปแล้ว 0, โอน 10000 (นับรวม) = ใช้ไป 10000
	# Limit = 40000. ลองถอนอีก 35000 (รวมเป็น 45000) ต้อง Error
	try:
		print("Attempting to withdraw 35,000 (Total daily: 45,000)...")
		harry_account.withdraw(atm_machine1, 35000)
		print("Error: Daily limit exceeded but not caught")
	except Exception as e:
		print(f"Pass: System correctly raised error -> {e}")

	print("\n--- Test Case #10 : ATM Insufficient Cash (Expect Error) ---")

	poor_atm = ATM_machine('9999', 100) 
	scb.add_atm_machine(poor_atm)
	try:
		print("Attempting to withdraw 500 from ATM with 100 THB...")
		harry_account.withdraw(poor_atm, 500)
		print("Error: ATM insufficient cash but not caught")
	except Exception as e:
		print(f"Pass: System correctly raised error -> {e}")

if __name__ == "__main__":
	run_test()