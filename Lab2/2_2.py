def allZero(arr) -> bool:
	for i in arr:
		if (i != 0):
			return False
	return True

def	main() -> None:
	user_input = input("Input : ").strip()
	for i in user_input:
		if (i.isdigit() == False and i.isspace() == False):
			print("Invalid Input")
			return
	user_input = user_input.split()
	arr = [int(x) for x in user_input]
	for x in arr:
		if (x > 9 or x < 0):
			print("Invalid Input")
			return
	if (allZero(arr) or len(arr) > 10):
		print("Invalid Input")
		return
	arr = sorted(arr)
	if (arr[0] == 0):
		for j, item2 in enumerate(arr):
			if (arr[j] != 0):
				temp = arr[0]
				arr[0] = arr[j]
				arr[j] = temp
				break
	print("".join([str(x) for x in arr]))

if __name__ == "__main__":
	main()