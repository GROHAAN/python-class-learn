# class student:
#     pass
# print(id(student))
# obj1 = student
# print(id(obj1)) # same address bcz each object refers to the samme student class
# obj2 = student
# print(id(obj2))

# class Student:
#     '''hello'''
#     schoool = 'shss'
#     def show_details():
#         print("welcome")
# print(dir(Student))
# print(Student.__doc__)

# class Student :
#     pass
# obj = Student()
# obj1 = Student()
# obj2 = Student()
# print(id(Student))
# print(id(obj),id(obj1),id(obj2))

# class Student:
#     def __init__(self): # python internal constuctor 
#         print('constructor called')
#         print(id(self))
# obj= Student()
# print(id(obj))

# class Student:
#     def __init__(self,name,quali):
#         self.n = name
#         self.q = quali
# obj1 = Student('abhi','b.com')
# obj2 = Student('shek','m.com')
# print(obj1.n)
# print(obj2.n)
        

#declaration of instance variable
# 1. inside class --> inside constructor
#                     inside instance method
# 2. outside class


#declaration of instance variable and calling


# class Student:
#     def __init__(self,name,roll_no):
#         self.n = name   #declaration
#         self.r = roll_no  #declaration
#         print(self.n,self.r)  #calling
#     def addnew(self,contact):
#         self.c = contact # declaration
#         print(self.n,self.r,self.c,self.city)  #caling
# obj = Student('abhi',101)
# x = eval(input("enter your contact details: "))
# obj.city = 'bhopal'
# obj.addnew(x)  #declaration
# print(obj.n,obj.c,obj.r)  #calling


# decalration of class variable( object independent variable)

# class Student:
#     school_name = 'abc school' # declaration
#     def  __init__(self,name,roll_no):
#         self.n,self.r = name,roll_no
#         Student.grade = '10th' #declaration
#         print(Student.school_name) #calling
#     def addnew(self):
#         Student.principal = 'python'  #declaration
#         print(Student.school_city)
# Student.school_city = 'bhopal' #declaration
# obj = Student('abhi',101)
# obj.addnew()
# print(Student.principal) #recommendation calling
        

#local variable

# class Student:
#     def __init__(self):
#         # global x
#         x = 10
#         print(x)
#     def new(self):
#         y = 10
#         print(y)
#         print(x)
# obj = Student()
# obj.new()


#class method
# class Book:
#     price = 100
#     def __init__(self,title,total_page):
#         self.t = title
#         self.tp = total_page
#     @classmethod
#     def update_price(cls,p):
#         cls.price = p
# obj = Book('python',500)
# print(obj.t,obj.tp,Book.price)
# x = float(input("enter updated price: "))
# obj.update_price(x)
# obj1 = Book('python',510)
# print(obj1.t,obj1.tp,Book.price)

#static method

# class Web:
#     def __init__(self,name):
#         self.n = name
#     @staticmethod
#     def greet ():
#         print('welcome to my web page')

# # obj = Web
# # obj.greet()

# obj= Web('ecom')
# obj.greet()

