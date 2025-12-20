def main() -> None:
	print(" *** integer summation from 1 to n ***")
	user_input = input("Enter an integer(n) : ").strip()
	ans = ""
	summation = 0
	for i in range(1, int(user_input)):
		ans += str(i)
		ans += "+"
		summation += i
	ans += user_input
	summation += int(user_input)
	print(f"Summation => {ans} = {summation}")

if __name__ == '__main__':
	main()