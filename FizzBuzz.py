def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        if grade < 39:
            roundedGrades.append(grade)
        else:
            for i in range(0, 100, 5):
                difference = i - grade
                if 0 < difference < 3:
                    roundedGrades.append(grade + difference)
                else:
                    roundedGrades.append(grade)

    return roundedGrades + "hi there"


grades = [4, 73, 67, 38, 33]
gradingStudents(grades)

