def main():
	user_input = input("Input : ")
	if (user_input.isdigit() == False):
		print("Invalid Input")
		return
	num = int(user_input)
	if (num < 0):
		print("Invalid Input")
		return
	for i in range(num, 0, -1):
		print("{}{}".format((i) * " ", (num - i + 1) * "#"))

if __name__ == "__main__":
	main()