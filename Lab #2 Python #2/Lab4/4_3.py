def main() -> None:
	print(" *** even integer summation from 1 to n ***")
	user_input = input("Enter an integer(n) : ").strip()
	ans = ""
	summation = 0
	for i in range(2, int(user_input), 2):
		ans += str(i)
		if (i < int(user_input) - 1):
			ans += "+"
		summation += i
	if (int(user_input) % 2 == 0):
		ans += user_input
		summation += int(user_input)
	print(f"Summation => {ans} = {summation}")

if __name__ == '__main__':
	main()