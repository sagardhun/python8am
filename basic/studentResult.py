subjects = ['Math', 'Science', 'English']
students = ['Ram', 'Syam', 'Hari']

num = int(input("Enter the number of students:"))
mak = []
x = 0
while x < num:

    print(f"=========Student{students[x]}======")
    mark = []
    for i in range(0, 3):
        marks = int(input(f"Enter the marks of {subjects[i]}:"))
        mark.append(marks)
    mak.append(mark)
    x += 1
print(mark)
print(mak)

result = []

for ms in mak:
    sum = 0
    for j in ms:
        sum += j
    result.append(sum)

print(result)
