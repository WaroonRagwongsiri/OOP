def main() -> None:
	print(" *** Arithmetic Sequence ***")
	user_input = input("Enter 2 numbers : ").strip()
	a1, r = [int(x.strip()) for x in user_input.split(" ")]
	for i in range(10):
		print(f"{a1 + r * (i)}", end=" ")
	print("")
	print("===== End of program =====")
if __name__ == '__main__':
	main()