def isPalindrome(s) -> bool:
	start = 0
	end = len(s) - 1
	while (start < end):
		if (s[start] != s[end]):
			return (False)
		start += 1
		end -= 1
	return (True)

def	main() -> None:
	userin = input("Enter digits : ")
	if (userin.isdigit() == False):
		print("Invalid Input")
		return
	num = int(userin)
	if (num < 1):
		print("Invalid Input")
		return
	maxpalin = 0
	for i in range(1 * (10**(num - 1)), 1 * (10**num)):
		for j in range(1 * (10**(num - 1)), 1 * (10**num)):
			if (isPalindrome(str(i * j)) and i * j > maxpalin):
				maxpalin = i * j
				break
	print(maxpalin)

if __name__ == "__main__":
	main()