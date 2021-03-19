# class Introduction:
#     def __init__(self):
#         print("python")
#
#     x = 10
#
#     def test(self):
#         print(self.x)
#
#
# obj = Introduction()
# ====================================================================================

class calculator:
    def take_value(self):
        c = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        return [c, b]

    def add():
        a = take_value()
        sum = a[0] + a[1]
        print(a[0])
        print(a[1])
        return sum

    # def display(self):
    #     s = a
    #     pass


obj = calculator()
obj.add()
