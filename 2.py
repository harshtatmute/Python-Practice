# class Student:
#     def __init__(self):
#         self.name = "Harsh"
#         self.age = 21

# s1 = Student()
# print(s1.name, s1.age)

# class Car:
#     def __init__(self, name, price):
#         self.brand = name
#         self.price = price

# c1 = Car("BMW", 500000)
# c2 = Car("TATA", 100000)

# print(c1.brand, c1.price)
# print(c2.brand, c2.price)

# print(c1.brand, c2.price)
# print(c2.brand, c1.price)


# Create a class:
# Employee
# Class variable → company = "Google"
# Instance variable → name, salary
# Create 2 employees:
# Harsh, 90000000
# Rahul, 60000000
# Print all values

class Employee:
    company = "Microsoft"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = Employee("Harsh", 90000000)
e2 = Employee("Rahul", 60000000)

print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)