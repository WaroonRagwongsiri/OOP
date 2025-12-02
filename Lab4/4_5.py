def f1(A, B, C):
	return f"{A}x + {B}y + {C} = 0"

def gcd_finder(A, B, C):
	A = abs(A)
	B = abs(B)
	C = abs(C)
	gcd = min(min(A, B), C)
	if (gcd == 0):
		return (1)
	while gcd > 0:
		if (A % gcd == 0 and B % gcd == 0 and C % gcd == 0):
			break
		gcd -= 1
	return (gcd)

def f2(A, B, C):
	gcd = gcd_finder(A, B, C)
	A = int(A / gcd)
	B = int(B / gcd)
	C = int(C / gcd)
	return f"{A}x + {B}y + {C} = 0"

def f3(A, B, C):
	gcd = gcd_finder(A, B, C)

	if (B < 0):
		op_b = "-"
		B = abs(B)
	else:
		op_b = "+"
	if (C < 0):
		op_c = "-"
		C = abs(C)
	else:
		op_c = "+"
	A = abs(int(A / gcd))
	B = abs(int(B / gcd))
	C = abs(int(C / gcd))
	A = "" if A == 1 else A
	B = "" if B == 1 else B
	C = "" if C == 0 else C
	if (C == ""):
		return f"{A}x {op_b} {B}y = 0"
	return f"{A}x {op_b} {B}y {op_c} {C} = 0"

def main() -> None:
	print(" *** Linear Formula ***")
	user_input = input("Enter x1 y1 x2 y2: ").strip()
	x1, y1, x2, y2 = [int(x.strip()) for x in user_input.split()]
	print(f"({x1},{y1}) ==> ({x2},{y2})")
	if (x1 == x2):
		print(f"Vertical line ==> x = {x1}.")
		print("===== End of program =====")
		return
	A = y2 - y1
	B = x1 - x2
	C = x2 * y1 - y2 * x1
	print(f"f1 ==> {f1(A, B, C)}")
	print(f"f2 ==> {f2(A, B, C)}")
	print(f"f3 ==> {f3(A, B, C)}")
	print("===== End of program =====")

if __name__ == '__main__':
	main()