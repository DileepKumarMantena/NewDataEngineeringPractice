students_grades = {
    "Preetham": "A",
    "John": "B",
    "Alice": "A+",
    "Emma": "B+",
    "David": "A-"
}


student_name = input("Enter the student's name to retrieve their grade: ")


if student_name in students_grades:
    print(f"{student_name}'s grade is: {students_grades[student_name]}")
else:
    print(f"Student {student_name} not found in the records.")