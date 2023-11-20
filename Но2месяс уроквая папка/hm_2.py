#№1
# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married

#     #№2
#     def introduce_myself(self):
#         print(f"Full name:{self.fullname}")
#         print(f"Age:{self.age}")
#         print(f"is married:{self.is_married}")

#№3
# class Teacher(Person):    
#     def __init__(self, fullname, age, is_married, experience):
#         super().__init__(fullname, age, is_married)
#         self.experience=experience
#         self.salary = 40000
    
#     def sum_salery(self):
#         for i in range(self.experience):
#             self.salary+=3000
#         print(f"ваша зарплата: {self.salary}")

# name=Teacher("Тургунбаева Кундуз",34,"да",4)
# name.introduce_myself()
# name.sum_salery()

