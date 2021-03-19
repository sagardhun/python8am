#insterting students marks
subjects=['english','nepali','math']

num = int(input("Enter number of students: "))

students = []
x = 1
while x <= num:
    print(f"======Student {x}======")
    store_maks = []
    for i in range(0, 3):
        mask = int(input(f"Enter {subjects[i]} marks"))
        store_maks.append(mask)

    students.append(store_maks)
    x+=1


#calculating total marks of each students
result = []
total = 0

for ms in students:
    total_mask = 0
    for a in ms:
        total_mask += int(a)

    result.append(total_mask)

for res in result:
    print(f"Result: {res}")
