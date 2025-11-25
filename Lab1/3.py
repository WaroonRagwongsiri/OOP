def	main():
	user_input = input().strip().split()

	if (len(user_input) != 4):
		print("Invalid Input")
		return

	h_in, m_in, h_out, m_out = user_input
	if (h_in < 7 or h_out > 23):
		print("Invalid Input")
		return
	
	t_in = h_in * 60 + m_in
	t_out = h_out * 60 + m_out
	time_passed = t_out - t_in
	if (time_passed <= 15):
		print(0)
	elif (time_passed <= 3 * 60):
		print(time_passed // 60 * 10)
	elif (time_passed <= 6 * 60):
		print(time_passed // 60 * 10)
	else:
		print(200)

if __name__ == "__main__":
	main()