student_marks = {
    "Aarav":  92,
    "Priya":  87,
    "Rohan":  75,
    "Sneha":  95,
    "Karan":  83
}

print("\n🏆 Student Marks:")
for student, marks in student_marks.items():
    grade = "A+" if marks >= 90 else "A" if marks >= 80 else "B"
    print(f"  {student}: {marks}/100  ({grade})")