def	main():
	a = input("Input : ")
	if (a.isdigit() == False or len(a) != 1):
		print("Output : Invalid Input")
		return
	a = float(a)
	print("Output :", int(a + a*11 + a*111 + a*1111))

if __name__ == "__main__":
	main()