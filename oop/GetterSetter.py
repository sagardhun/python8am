class GetterSetter:

    def __init__(self):
        print("I am init method.")

    def __new__(cls):
        print("I am new method")
        return object(cls)