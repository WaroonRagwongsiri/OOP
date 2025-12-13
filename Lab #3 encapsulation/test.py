from lab3 import Subject, Teacher, Student

s1 = Subject("1", "1", 1)
s2 = Subject("2", "2", 2)
s3 = Subject("3", "3", 3)

setto = set((s2, s3))

setto.add(s1)

if s1 in setto:
	print("In")
else:
	print("No")