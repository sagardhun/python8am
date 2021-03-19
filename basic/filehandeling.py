# handle=open('record.txt', 'w')
# handle.write("hello python")
# handle.close()

# handle=open('record.txt', 'w')
# handle.a=int(input("enter any number:"))
# handle.b=int(input("enter sec number:"))
# handle.write("sum of given numbers is:",a+b)
# handle.close()

# ========================================================================================
# obj = open("record.txt", 'w')
#
# x = int(input("enter number:"))
# y = int(input("enter number:"))
#
# result = x + y
#
#
# def insert():
#     pass
#
#
# def show():
#     pass
#
#
# def update():
#     pass
#
#
# def deletee():
#     pass
# =====================================================================================================================
'''
import os

if not os.path.exists('database.txt'):
    fh = open('database.txt', 'w')
    fh.close()


def register():
    username = input("Enter username:")
    if username in open('database.txt', 'r'):
        print("Username already exists.")
        exit()

    password = input("Enter password:")
    c_password = input("conform password:")

    if password != c_password:
        print("Enter same password.")
        exit()

    handle = open('database.txt', 'a')

    handle.write(username)
    handle.write("  ")
    handle.write(password)
    handle.write("\n")
    handle.close()

    print("User successfully registered.")


def login():
    username = input("Enter username:")
    password = input("Enter password:")

    get_record = open('database.txt', 'r').readline()

    print(get_record)


register()
login()

'''


