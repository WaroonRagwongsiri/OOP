empty_str = [
	'""',
	"''",
	'" "',
	"' '",
	"",
	" ",
]

def add_score(subject_score: dict, subject: str, score) -> dict:
	if (subject in empty_str):
		return
	if ('.' in score):
		score = float(score)
	else:
		score = int(score)
	if (score < 0):
		return
	subject_score[subject.strip("'")] = score

def calc_average_score(subject_score: dict) -> float:
	sum = 0
	if (len(subject_score) == 0):
		return 0
	for keys, item in subject_score.items():
		if (float(item) < 0):
			raise Exception
		sum += float(item)
	avg = sum / len(subject_score)
	avg = float(avg)
	return avg

def main() -> None:
	user_input = input("Input : ").strip()
	user_input = user_input.split('|')
	subject_score, subject, score = [x.strip() for x in user_input]
	subject_score = dict(eval(subject_score))
	add_score(subject_score, subject, score)
	avg_score = calc_average_score(subject_score)
	print("{}, Average score: {:.2f}".format(subject_score, avg_score))

if __name__ == '__main__':
	main()
