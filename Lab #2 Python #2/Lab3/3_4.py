empty_str = [
	'""',
	"''",
	'" "',
	"' '",
	"",
	" ",
	'',
]

def add_score(subject_score: dict, student: str, subject: str, score: str) -> dict:
	if '.' in score:
		score = float(score)
	else:
		score = int(score)
	if score < 0:
		raise Exception
	# No student in subject_score
	if not (student in subject_score):
		subject_score[student] = {}
	subject_score[student][subject.strip("'")] = score

def calc_average_score(subject_score: dict) -> float:
	avg_score = {}
	for student, student_score in subject_score.items():
		if str(student).isnumeric() == False:
			raise Exception
		avg = 0
		student_score = dict(student_score)
		for subj, score in student_score.items():
			avg += score
		avg /= len(student_score)
		avg_score[student] = f"{avg:.2f}"
	return avg_score

def main() -> None:
	try:
		user_input = input("Input : ").strip()
		user_input = user_input.split('|')
		user_input = [x.strip() for x in user_input]
		subject_score = user_input[0]
		user_input = user_input[1::]
		subject_score = dict(eval(subject_score))
		if (len(user_input) % 3 != 0):
			raise Exception
		for i in range(2, len(user_input), 3):
			student = user_input[i - 2]
			subject = user_input[i - 1]
			score = user_input[i]
			if (student in empty_str) or (subject in empty_str) or (score in empty_str) or (student.isdigit() == False):
				raise Exception
			add_score(subject_score, student, subject, score)
		avg = calc_average_score(subject_score)
		print(f"{subject_score}, Average score: {avg}")
	except:
		print("Invalid")

if __name__ == '__main__':
	main()
