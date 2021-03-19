# def test():
#     print("hello")
#
# test()
# test()
# ==============================================
# def pi():
#     3.14
#
# r=2
# p=r*pi()
# print(p)
# ===============================================
# def test():
#     return"hello"
# print(test())
# ==============================================
# def users(name, age):
#     print(name)
#     print(age)
#
# users()

# ===========================================
# def users(name, age):
#     print(name)
#     print(age)
#
#
# users('ram', 20)
# users('sita', 30)

# ===================================================

# def addsub(x, y):
#     add = x + y
#     sub = 0
#     if x > y:
#         sub = x - y
#     else:
#         sub = y - x
#     return [add, sub]
#
#
# a = addsub(10, 20)
# print(a[0])
# print(a[1])

# ======================================================

# def user(name, age=0):
#   print(name)
#    if age > 0:
#        print(age)
#

# user('ram')
# ===============================================
# ptr/100
# def takeinput():
#   pass


# def calculator():
#   pass


# def result():
#   pass


# ===============================================

# def myrep(data, times)
#  pass


# myrep('ram', 20)

#       def takeinput():
#          p = int(input("Enter the principle amount:"))
#           t = int(input("Enter the time period:"))
#          r = input("Enter the rate of interest:")
#           return [p, t, r]


#     def calculator():
#        data = takeinput()
#           return i[0] * i[1] * i[2] / 100


#  def result():
#     print("Total amount of interest is found to be ",calculator())


# result()


def my_rep():
    data = input("Enter the data:")
    times = int(input("Enter the number of times:"))
    x = 0
    while x <= times:
        print(data)
        x += 1


my_rep()
