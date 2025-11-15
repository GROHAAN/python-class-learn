# class Student:
#     x= 10
#     y = 20
#     def new (self):
#         print("from new")
# obj = Student()

# Inheritance Single Level 
# class Parent:
#     car = "maruti suzuki"
#     def home (self):
#         print("home from parent")
# class Child(Parent):
#     pass
# obj = Child()
# print(obj.car)
# obj.home()

# Method overriding

class Parent:
    car = "nexon"
    def home(self):
        print("home from parents")
class Child(Parent):
    def home(self):
        print("home from child")
        # super().home() # used to access parent home 
obj = Child()
obj.home()