def main() -> None:
	print(" *** Transform to seconds ***")
	user_input = input("Enter h m s : ").strip().split()
	user_input = [int(x) for x in user_input]
	h, m, s = user_input
	sec = str(60*60*h + 60*m + s)
	rev_sec = list(sec[::-1])
	for index, item in enumerate(rev_sec):
		if (index % 3 == 0 and index != 0):
			rev_sec.insert(index, ",")
	rev_sec = "".join(rev_sec)
	sec = rev_sec[::-1]
	print(h, "hours", m, "minutes", s, "seconds", "=", sec, "seconds")

if __name__ == "__main__":
	main()