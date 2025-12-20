def is_leap(year: int) -> bool:
	try:
		if (year < 0):
			raise Exception
		return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	except:
		return "False"

def day_of_year(day: int, month: int, year: int) -> int:
	day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	try:
		if (day < 1 or month < 1 or year < 0):
			raise Exception
		day_of_years = 0
		if is_leap(year):
			day_in_month [2] += 1
		else:
			if month == 2 and day == 29:
				raise Exception
		if (day > day_in_month[month] or month > 12):
			raise Exception
		for i in range(1, month):
			day_of_years += day_in_month[i]
		day_of_years += day
		return day_of_years
	except:
		return "Invalid"

def day_in_year(year: int) -> int:
	return 365 + is_leap(year)

def date_diff(time1, time2):
	try:
		diff = 0
		d1, m1, y1 = [int(x) for x in time1.split("-")]
		d2, m2, y2 = [int(x) for x in time2.split("-")]
		if (y1 > y2):
			return "Invalid"
		elif (y1 == y2):
			return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1
		diff += day_in_year(y1) - day_of_year(d1, m1, y1)
		diff += day_of_year(d2, m2, y2)
		for i in range(y1 + 1, y2):
			diff += day_in_year(i)
		return diff + 1
	except:
		return "Invalid"

def main():
	try:
		user_input = input("Enter Input: ")
		user_input = user_input.strip().split(',')
		time1, time2 = [x.strip() for x in user_input]
		diff = date_diff(time1, time2)
		print(diff)
	except:
		print("Invalid")
		
if __name__ == '__main__':
	main()