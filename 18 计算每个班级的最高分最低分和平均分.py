# key: course, value: garde list

course_grade = {}

with open("course_student_grade_input.txt") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, grade = line.split(",")
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(int(grade))

print(course_grade)

for course, grades in course_grade.items():
    print(
        course,
        max(grades),
        min(grades),
        sum(grades)/len(grades),
    )