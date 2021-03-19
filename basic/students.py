'''def student():
    names = []
    i = 0
    number_of_students = int(input("Enter the number of students:"))

    while i < number_of_students:
        name = input("Enter the name of the student:")
        i += 1
        names.append(name)
    print(names)


student()


def subjects():
    sub = []
    j = 1
    number_of_subjects = int(input("Enter the number of subjects:"))
    while j <= number_of_subjects:
        subject = input("Enter the subject name:")
        j += 1
        sub.append(subject)

    print(subject)


subjects()


def score():
    for k in range(0, number_of_students):
        name = student(k)
    for l in range(0, number_of_subjects):
        subj = subjects(l)

    print(subjects[1])
    print(student[1])


score()
'''
'''data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

for i in range(0, 4):
    for j in range(0, 4):
        if data[i][j] == 13 and data[i][j] == 18:
            print(data[i][j])


'''
'''
import database

print(database.insert())
print(database.update())
print(database.data)

from database import insert, update
from demo import insert as ins
# from database import *

print(insert())
print(update())
print(ins())
==================================================================
'''
'''
=====================================================================
import csv

print(dir(csv))

with open('data.csv', 'r')as file:
    get_data=csv.reader(file)
    for user in get_data:
        print(user)
'''


