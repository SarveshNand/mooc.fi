# Write your solution here
def add_student(students: dict, name: str):
    students[name] = {"courses": {}}

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    courses = students[name]["courses"]

    if not courses:
        print(f"{name}:\n no completed courses")
        return

    print(f"{name}:")
    print(f" {len(courses)} completed courses:")

    total = 0

    for course, grade in courses.items():
        print(f"  {course} {grade}")
        total += grade

    avg = total / len(courses)
    print(f" average grade {avg}")

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course

    if grade == 0:
        return

    courses = students[name]["courses"]

    if course_name not in courses:
        courses[course_name] = grade
    else:
        if grade > courses[course_name]:
            courses[course_name] = grade

def summary(students: dict):
    print(f"students {len(students)}")

    most_courses_name = ""
    most_courses_count = 0

    best_avg_name = ""
    best_avg = 0

    for name, data in students.items():
        courses = data["courses"]

        count = len(courses)

        if count > most_courses_count:
            most_courses_count = count
            most_courses_name = name

        if count > 0:
            avg = sum(courses.values()) / count

            if avg > best_avg:
                best_avg = avg
                best_avg_name = name

    print(f"most courses completed {most_courses_count} {most_courses_name}")
    print(f"best average grade {best_avg} {best_avg_name}")