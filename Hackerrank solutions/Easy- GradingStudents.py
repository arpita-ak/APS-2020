"""
Grading Students: https://www.hackerrank.com/challenges/grading/problem

"""
import os

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<38:
            continue
        elif ((grades[i]+1)%5 == 0):
            grades[i]+=1
        elif ((grades[i]+2)%5 == 0):
            grades[i]+=2
        else:
            continue

    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
