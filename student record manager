student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
    print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["grades"].add(grade)
    print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    grades = student_records[name]["grades"]
    if not grades:
        return 0
    return sum(grades) / len(grades)

def list_students_by_course(course):
    students_in_course = []
    for name, details in student_records.items():
        if course in details["courses"]:
            students_in_course.append(name)
    return students_in_course

def filter_top_students(threshold):
    top_students = []
    for name in student_records:
        if calculate_average_grade(name) > threshold:
            top_students.append(name)
    return top_students


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
