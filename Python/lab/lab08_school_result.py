import sys

print("SCHOOL RESULT PROCESSING")

name = input("Enter Student Name : ")
roll_no = input("Enter Roll Number  : ")
print()
print("Enter Marks for 5 Subjects (0-100)")
total_marks = 0.0
failed_subject = False
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        sys.exit()
    if mark < 40:
        failed_subject = True
    total_marks += mark
percentage = (total_marks / 500) * 100
if failed_subject:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        result = "FAIL"
        grade = "F"
        remark = "Fail"
print()
print("STUDENT REPORT CARD")

print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll_no}")
print()
print(f"  Total Marks  : {total_marks} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")

