
day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	try:
		if (year < 0):
			raise Exception
		return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	except:
		return "False"

def day_of_year (day, month, year):
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

def main():
	try:
		user_input = input("Enter a date : ").strip().split('-')
		day, month, year = [int(x) for x in user_input]
		doy = day_of_year(day, month, year)
		leap = is_leap(year)
		print("day of year: {} ,is_leap: {}".format(doy, leap))
		return
	except:
		if len(user_input) != 3:
			print("day of year: {} ,is_leap: {}".format("Invalid", "False"))
			return
		day, month, year = user_input
		if (year.isnumeric() == False):
			print("day of year: {} ,is_leap: {}".format("Invalid", "False"))
			return
		print("day of year: {} ,is_leap: {}".format("Invalid", is_leap(int(year))))

if __name__ == '__main__':
	main()