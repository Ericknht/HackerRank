if __name__ == '__main__':
    python_students = [['Harry', 37.21],
                        ['Berry', 37.21],
                        ['Tina', 37.2],
                        ['Akriti', 41],
                        ['Harsh', 39]]

    python_students.sort(key=lambda x: x[1])

    first_score = python_students[0][1]
    second_score = None
    second_students_name = list()

    for student in python_students:
        if student[1] > first_score:
            second_score = student[1]
            break

    for student in python_students:
        if student[1] == second_score:
            second_students_name.append(student[0])

    second_students_name.sort()
    for student in second_students_name:
        print(student)
