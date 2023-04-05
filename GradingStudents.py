import random
import math

def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    for grade in grades:
        if grade < 38:
            roundedGrades.append(grade)
        else:
          for i in range(0, 101, 5):
            difference = i - grade
            if 0 <= difference < 5:
              if 0 <= difference < 3:
                roundedGrades.append(grade + difference)
              else:
                roundedGrades.append(grade)

    return roundedGrades

#Checking The Code For Randoms Cases
list = []

for i in range(10):
  list.append(math.ceil(random.random()*100))
list[0] = 100

print(list)
print(gradingStudents(list))


