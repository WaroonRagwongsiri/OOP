from lab3 import Subject, Teacher, Student

subject1 = Subject("1", "1", 1)

student1 = Student("1", "Name")

res1 = student1.enroll(subject1)
print(f" - Enroll CS101: {res1} (Expected: Done)")