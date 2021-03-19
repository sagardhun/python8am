class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    x = 10

    def get_brand(self):
        return f"Brand Name : {self.brand}"

    def get_price(self):
        return f"Price Rs.: {self.price}"


class Mi(Mobile):
    def __init__(self, brand, price, company):
        super().__init__(brand, price)
        self.cmp = company

    def get_company(self):
        return f"Company Name: {self.cmp}"


obj = Mi("Abc", 1000, 'Test')
print(obj.get_price())
print(obj.get_brand())
print(obj.get_company())
#design pattern
