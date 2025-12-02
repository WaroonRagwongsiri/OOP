def main() -> None:
	print(" *** Power of n ***")
	user_input = input("Enter n num : ").strip()
	n, num = [int(x.strip()) for x in user_input.split()]
	i = 1
	while (n ** i <= num):
		if (n ** i == num):
			print("{0} is the power of {1}.".format(num, n))
			print("{0} = {1}".format(num, "{0}*".format(n) * (i - 1) + str(n)))
			print("===== End of program =====")
			return
		i += 1
	print("{0} is NOT the power of {1}.".format(num, n))
	print("===== End of program =====")

if __name__ == '__main__':
	main()
