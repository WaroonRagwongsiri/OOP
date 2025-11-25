def	main():
	user_in = input("Enter your input : ").strip()
	if (user_in == "[]"):
		print("Invalid Input")
		return
	for i, item in enumerate(user_in):
		if (i == 0 and item != '['):
			print("Invalid Input")
			return
		if (i == len(user_in) - 1 and item != ']'):
			print("Invalid Input")
			return
		if (item.isdigit() == False and item.isspace() == False and item not in ",-+" and i != 0 and i != len(user_in) - 1):
			print("Invalid Input")
			return
		if ((item == '[' or item == ']') and i != 0 and i != len(user_in) - 1):
			print("Invalid Input")
			return

	user_in = user_in[1:-1:].split(',')
	arr = [int(x) for x in user_in]
	
	max = 0
	if (len(arr) == 0 or len(arr) == 1):
		print("Invalid Input")
		return
	for i, i1 in enumerate(arr):
		for j, i2 in enumerate(arr):
			if (i == 0 and j == 1):
				max = i1 * i2
			else:
				if (i != j and i1 * i2 > max):
					max = i1 * i2
	print(max)

if __name__ == "__main__":
	main()