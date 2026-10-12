def student(first_name, last_name, age, level, department="ICT Education"):
    student_details = f"{first_name} {last_name} {age} {level} "
    print(student_details) 

def courses (*courses):
    for course in courses:
        print(course)

def fees():
    print(f"pay your fees ")