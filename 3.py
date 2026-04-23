# class Laptop:
#     def __init__(self,Brand,RAM):
#         self.brand = Brand
#         self.ram = RAM

# laptop1 = Laptop("HP", "16GB")
# laptop2 = Laptop("Dell", "8GB")

# print(laptop1.brand , laptop1.ram)
# print(laptop2.brand , laptop2.ram)

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
    
#     def display(self):
#         print (self.brand) 
#         print(self.price)

# m1 = Mobile("Apple", 120000)
# m1.display()

class company:
    company = "Google"

    def __init__(self,Name):
        self.name = Name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    def display(self):
        print(self.name)

e1 = company("Harsh Tatmute")
print(e1.name)

print(e1.company)

e1.display()

e1.change_company("Microsoft")
print(e1.company)

""" Output -->  Harsh Tatmute, Google,  Harsh Tatmute,  Microsoft """
