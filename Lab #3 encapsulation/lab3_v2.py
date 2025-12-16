# =============================================================================
# ส่วนที่ 1: พื้นที่สำหรับนักศึกษา (Student Implementation Area)
# =============================================================================

from typing import Literal

class Enrollment:
	def __init__(self, subject: 'Subject'):
		self.__subject = subject
		self.__grade = None

	def get_subject(self):
		return self.__subject
	
	def set_grade(self, grade):
		self.__grade = grade

	def get_grade(self):
		return self.__grade

	subject = property(get_subject)
	grade = property(get_grade, set_grade)

class Student:
	def __init__(self, id: str, student_name: str):
		self.__id = id
		self.__student_name = student_name
		self.__enrolled_subject = list()

	def enroll(self, subject: 'Subject') -> str:
		"""
			enroll to the subject

			Input
				subject - Subject for student to enroll

				subject : Subject
			Return
				status - "Done", "Already Enrolled", "Error"

				status : str
		"""
		try:
			if not isinstance(subject, Subject):
				raise TypeError

			for index, item in enumerate(self.__enrolled_subject):
				enrollment: Enrollment = item
				if subject == enrollment.subject:
					return "Already Enrolled"

			new_enroll = Enrollment(subject)
			self.__enrolled_subject.append(new_enroll)
			return "Done"
		except Exception as e:
			return "Error"

	def drop(self, subject: 'Subject') -> str:
		"""
			drop to the subject

			Input
				subject - Subject for student to drop

				subject : Subject
			Return
				status - "Done", "Not Found", "Error"

				status : str
		"""
		try:
			if not isinstance(subject, Subject):
				raise TypeError

			found = -1
			for index, item in enumerate(self.__enrolled_subject):
				enrollment: Enrollment = item
				if subject == enrollment.subject:
					found = index
					break
			if found == -1:
				return "Not Found"

			return self.__enrolled_subject.pop(found)
		except:
			return "Error"

	def assign_grade(self, subject: 'Subject', grade: Literal["A", "B", "C", "D", "F"]):
		"""
			assign grade to subject

			Input
				subject - Subject for student to drop
				grade - "A", "B", "C", "D", "F"

				subject : Subject
				grade - Literal["A", "B", "C", "D", "F"]
			Return
				None
		"""
		accept_grade = ["A", "B", "C", "D", "F"]
		if not (grade in accept_grade) or not isinstance(grade, str):
			return "Error"

		if not isinstance(subject, Subject) or not isinstance(grade, str):
			raise TypeError

		found = -1
		for index, item in enumerate(self.__enrolled_subject):
			enrollment: Enrollment = item
			if subject == enrollment.subject:
				found = index
				break
		if found == -1:
			return "Not Found"

		if grade == "A":
			self.__enrolled_subject[found].grade = 4
		if grade == "B":
			self.__enrolled_subject[found].grade = 3
		if grade == "C":
			self.__enrolled_subject[found].grade = 2
		if grade == "D":
			self.__enrolled_subject[found].grade = 1
		if grade == "F":
			self.__enrolled_subject[found].grade = 0
		return "Done"

	def get_enrolled_subjects(self):
		"""
			Get enrollled subject

			Input
				None
			Return
				enrolled_subject - set of enrolled subject

				enrolled_subject - list()
		"""
		return self.__enrolled_subject

	def get_gps(self) -> float:
		"""
			get gps from student

			Input
				None
			Return
				gps - gps of student

				gps - float
		"""
		all_score = 0
		all_credit = 0

		for index, item in enumerate(self.__enrolled_subject):
			enrollment: Enrollment = item
			grade = enrollment.grade
			credit = enrollment.subject.credit

			if grade == None:
				continue

			all_score += grade * credit
			all_credit += credit

		return all_score / all_credit

class Teacher:
	def __init__(self, id: str, teacher_name: str):
		self.__id = id
		self.__teacher_name = teacher_name

class Subject:
	def __init__(self, id: str, subject_name: str, credit: int):
		self.__id = id
		self.__subject_name = subject_name
		self.__credit = credit
		self.__teacher = set()
		self.__student = list()
		self.__student_score = list()
	
	def assign_teacher(self, teacher: Teacher):
		"""
			Assign Teacher to the subject

			Input
				teacher - Teacher for a subject

				teacher - Teacher
			Return
				None
		"""
		if not isinstance(teacher, Teacher):
			raise TypeError
		self.__teacher.add(teacher)

	def get_credit(self):
		"""
			get credit for subject
		"""
		return self.__credit

	credit = property(fget=get_credit)

# =============================================================================
# ส่วนที่ 2: Test Script (ใช้งานร่วมกับ Code ด้านบน)
# =============================================================================

def run_tests():
	print("---------------------------------------")
	print("Testing Student Registration System (Full Test Suite)")
	print("---------------------------------------")

	# --- Setup Data (เตรียมข้อมูล) ---
	teacher1 = Teacher('T001', "Mr. Welsh")
	subject1 = Subject('CS101', "Computer Programming 1", 3)
	subject2 = Subject('CS102', "Computer Programming 2", 3)
	subject3 = Subject('CS103', "Data Structure", 4)
	
	# Test Setup: Assign Teacher
	try:
		subject1.assign_teacher(teacher1)
		print(f"Setup Teacher: PASS") 
	except Exception as e:
		print(f"Setup Teacher: FAIL ({e})")

	student1 = Student('66010001', "Keanu Welsh")
	student2 = Student('66010002', "Khadijah Burton")

	# ---------------------------------------------------------
	# Test Case 1: Enrollment Logic (การลงทะเบียน)
	# ---------------------------------------------------------
	print("\n[1] Testing Enrollment Logic")
	
	# 1.1 ลงทะเบียนปกติ
	res1 = student1.enroll(subject1)
	print(f" - Enroll CS101: {res1} (Expected: Done)")
	
	# 1.2 ลงทะเบียนซ้ำ
	res2 = student1.enroll(subject1)
	print(f" - Enroll CS101 Again: {res2} (Expected: Already Enrolled)")
	
	# 1.3 ลงทะเบียนวิชาเพิ่ม
	student1.enroll(subject2)
	print(f" - Enroll CS102: Done")

	# ---------------------------------------------------------
	# Test Case 2: Drop Logic (การถอนรายวิชา)
	# ---------------------------------------------------------
	print("\n[2] Testing Drop Logic")
	
	# 2.1 ถอนรายวิชาที่มีอยู่
	res_drop = student1.drop(subject2)
	print(f" - Drop CS102: {res_drop} (Expected: Done)")
	
	# 2.2 ตรวจสอบว่าวิชาหายไปจริงหรือไม่
	subjects = student1.get_enrolled_subjects()
	if len(subjects) == 1 and list(subjects)[0] == subject1:
		print(" - Verify Remaining Subjects: PASS")
	else:
		print(f" - Verify Remaining Subjects: FAIL (Found {len(subjects)} subjects)")

	# ---------------------------------------------------------
	# Test Case 3: GPA Calculation (การคำนวณเกรดเฉลี่ย)
	# ---------------------------------------------------------
	print("\n[3] Testing GPA Calculation")
	
	# Setup: ลง 3 วิชา
	student2.enroll(subject1)
	student2.enroll(subject2)
	student2.enroll(subject3)
	
	# ใส่เกรด
	student2.assign_grade(subject1, "A") # 3 หน่วยกิต * 4 = 12
	student2.assign_grade(subject2, "B") # 3 หน่วยกิต * 3 = 9
	student2.assign_grade(subject3, "C") # 4 หน่วยกิต * 2 = 8
	# Total Points = 29, Total Credits = 10 -> GPA = 2.90
	
	gps = student2.get_gps()
	print(f" - Student2 GPS: {gps:.2f} (Expected: 2.90)")

	# ---------------------------------------------------------
	# Test Case 4: Grade Update (การแก้ไขเกรด)
	# ---------------------------------------------------------
	print("\n[4] Testing Grade Update")
	
	# เปลี่ยนเกรดวิชา CS102 จาก B เป็น A
	student2.assign_grade(subject2, "A") 
	# Points เดิม 29 -> เพิ่มมา 3 แต้ม (เพราะ B->A ต่างกัน 1 คะแนน * 3 หน่วยกิต) = 32
	# GPA ใหม่ = 32 / 10 = 3.20
	
	new_gps = student2.get_gps()
	print(f" - Student2 New GPS: {new_gps:.2f} (Expected: 3.20)")

	# ---------------------------------------------------------
	# Test Case 5: Edge Cases (กรณีพิเศษ)
	# ---------------------------------------------------------
	print("\n[5] Testing Edge Cases")
	student_fresh = Student('999', "Freshy")
	
	# 5.1 ยังไม่ลงทะเบียนเลย
	print(f" - No Subjects GPS: {student_fresh.get_gps()} (Expected: 0.0)")
	
	# 5.2 ลงทะเบียนแล้ว แต่ยังไม่มีเกรด
	student_fresh.enroll(subject1)
	print(f" - No Grade GPS: {student_fresh.get_gps()} (Expected: 0.0)")

	# ---------------------------------------------------------
	# Test Case 6: Robustness (ทดสอบความทนทาน - Type Check)
	# ---------------------------------------------------------
	print("\n[6] Testing Robustness (Object vs String)")
	
	# 6.1 Enroll ด้วย String
	try:
		res = student_fresh.enroll("CS101 String")
		if res == "Error":
			print(f" - Enroll with String: PASS (Correctly returned 'Error')")
		else:
			print(f" - Enroll with String: FAIL (Returned '{res}', Expected 'Error')")
	except AttributeError:
		print(" - Enroll with String: CRASHED ❌ (Code tried to access string attributes)")
	except Exception as e:
		print(f" - Enroll with String: CRASHED ({e})")

	# 6.2 Drop ด้วย String
	try:
		res = student_fresh.drop("CS101 String")
		if res == "Error":
			print(f" - Drop with String: PASS (Correctly returned 'Error')")
		else:
			print(f" - Drop with String: FAIL (Returned '{res}', Expected 'Error')")
	except Exception as e:
		print(f" - Drop with String: CRASHED ({e})")

	# ---------------------------------------------------------
	# Test Case 7: Logic Consistency (ความสอดคล้องของข้อมูล)
	# ---------------------------------------------------------
	print("\n[7] Testing Logic Consistency (Non-enrolled Subjects)")
	
	# 7.1 Drop วิชาที่ไม่ได้ลงทะเบียน (student1 ถอน CS102 ไปแล้วใน Case 2)
	# ลองถอน CS103 ที่ไม่เคยลงเลย
	res_drop_not_found = student1.drop(subject3) 
	if res_drop_not_found == "Not Found":
		print(f" - Drop Non-enrolled Subject: PASS (Returned 'Not Found')")
	else:
		print(f" - Drop Non-enrolled Subject: FAIL (Returned '{res_drop_not_found}', Expected 'Not Found')")

	# 7.2 ให้เกรดวิชาที่ไม่ได้ลงทะเบียน
	res_grade_not_found = student1.assign_grade(subject3, "A")
	if res_grade_not_found == "Not Found" or res_grade_not_found == "Error":
		print(f" - Grade Non-enrolled Subject: PASS (Returned '{res_grade_not_found}')")
	else:
		print(f" - Grade Non-enrolled Subject: FAIL (Returned '{res_grade_not_found}', Expected 'Not Found')")

if __name__ == "__main__":
	run_tests()