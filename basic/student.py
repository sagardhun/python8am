num = int(input("Enter the number of student:"))
subjects = ['Math', 'Science', 'English']
mak = []
x = 1
while x <= num:
    print(f"=============STUDENT{x}===========")
    mark = []
    for i in range(0, 3):
        marks = int(input(f"Enter the marks of {subjects[i]}:"))
        mark.append(marks)
    mak.append(mark)
    x += 1

print(mak)

total_marks = 0
result = []

for ms in mak:
    sum = 0
    for a in ms:
        sum = sum + a
    result.append(sum)
print(result)
for i in result:
    res = i * 100 / 300
    print("percentage=", res)