# for, while, nested loop

# data = ['ram', 'gita', 'sita', 'hari']
#
# for users in data:
#     print(users[0])

#
# data = [
#     ['ram', 'gita', 'sita', 'hari'],
#     ['kabita', 'babita', 'syam', 'krishna'],
#     ['rita', 'sophia', 'hita', 'ramita']
# ]
# for users in data:
#     for user in users:
#         if user == 'babita' or user == 'ramita':
#             print(user)
# =======================================================================================================================
# x = 0

# while x < 10:
#     print(x)
#     x += 1
# ======================================================================================================================
# number of student=5
# enter name 5 times should vome
# 5 neme should be printed
#
# even and odd
#
#
# no of student
# if 5
#     5 times subject mask should be entered
#


# =======================================================================================================================
# x = int(input("Enter any number:"))
# u = 1
# while u <= x:
#     if u % 2 == 0:
#         print("even:", u)
#
#     else:
#         print("odd:", u)
#     u += 1

# ======================================================================================================================

num = int(input("Enter the number of students:"))
x = 1
users=[]

while x <= num:
    name = input(f"Enter the name of roll  {x}  student:")
    x += 1
    users.append(name)

print(users)

for user in users:
    print(user)