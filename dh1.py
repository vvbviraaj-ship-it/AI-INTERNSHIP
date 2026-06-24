import json
student = {
    "name": "riya",
    "marks": "99"}

with open("student.jason", "w") as file:
    json.dump(student,file)