def	main():
	user_input = input("Enter your input : ").strip().split()

	if (len(user_input) != 4):
		print("Invalid Input")
		return

	for i in user_input:
		if (i.isdigit() == False):
			print("Invalid Input")
			return

	h_in, m_in, h_out, m_out = user_input
	h_in = int(h_in)
	m_in = int(m_in)
	h_out = int(h_out)
	m_out = int(m_out)

	t_in = (h_in * 60) + m_in
	t_out = (h_out * 60) + m_out

	if (t_in < 7 * 60 or t_in > 23 * 60
		or t_out < 7 * 60 or t_out > 23 * 60
		or m_in > 59 or m_out > 59
		or m_in < 0 or m_out < 0
		or h_in < 7 or h_in > 23
		or h_out < 7 or h_out > 23):
		print("Invalid Input")
		return

	time_passed = t_out - t_in

	if (time_passed < 0):
		print("Invalid Input")
	elif (time_passed <= 15):
		print(0)
	elif (time_passed <= (3 * 60)):
		print(int(((time_passed // 60) + (time_passed % 60 != 0)) * 10))
	elif (time_passed <= (6 * 60)):
		print(int((((time_passed - (3 * 60)) // 60) + ((time_passed - (3 * 60)) % 60 != 0)) * 20 + 30))
	else:
		print(200)

if __name__ == "__main__":
	main()