Student_marks = {"Aisha": 88,
"Rohan ": 75,
"Priya": 92,
"Amit": 63,
"Sneha": 81,
"Rahul": 70,
"Diya": 95,
"Vikram": 68,
"Ishita": 89,
"Arjun": 77}

name = input("Enter the student's name: ")

if name in Student_marks:
    print("{}'s marks : {}".format(name,Student_marks.get(name)))
else:
    print("Student not found")
