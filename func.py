# def display():
#     print('hello')
# print(display())

# def display():
#     print('hello')
# display()

# def display():
#     print('hello')
# x = display()

# def display():
#     print('hello')
# x = display()
# print(x)
# print(x)
# print(x)

# def display():
#     return "hello"
# print(display())

# def display():
#     return "hello"
# x = display()


# def display():
#     return 
# x = display()
# print(x)
# print(x)
# print(x)

# Positional arguments
# def fun_name (x,y,z):
#     print(f'x= {x} y= {y} z= {z}')
# p = int(input('enter any value: '))
# q = int(input('enter any value: '))
# r = int(input('enter any value: '))

# fun_name(p,q,r)


# default Arguments
# def fun_name (x= 0,y= 0,z= 0):
#     print(f'x= {x} y= {y} z= {z}')
# # fun_name(10,20,30)
# # fun_name()
# fun_name(10,20)

# vairable length positional arguments

# def fun_name(* args):
#     print(args)
#     print(type(args))
# t = eval(input("enter any tuple: "))
# fun_name(t)
# # fun_name(10,20,30,'python',49,50)

# def add_all (* n):
#     sum = 0
#     for i in n:
#         sum = sum + i
#     print(f'sum is {sum}')

# add_all(10,20,30,30,40)

# def add_all (* n):
#     sum = 0
#     for i in n:
#         for j in i:
#             sum = sum + j
#     print(f'sum is {sum}')

# var = eval(input('Enter any collection: '))
# add_all(var)

# def add_all (* n):
#     sum = 0
#     # for i in n:
#     #     for j in i:
#     #         sum = sum + j
#     # print(f'sum is {sum}')
#     print(n)
#     for i in n:
#         sum= sum+i
#     print(f'sum is {sum}')

# var = eval(input('Enter any collection: '))
# add_all(* var)


#errors 
# def display (x = 0, y):
#     print(f'{x,y}')
# display(10,20)


# def display (* n,x):
#     print (f'{n,x}')

# display(10,20,30)

# def display (x,y=0, * z):
#     print(f'{x,y,z}')
# display(10,20,30,40,50)


# Keyword Argument

# def fun (x,y,z):
#     print(f'{x,y,z}')
# fun(x=10,y=20,z=40)

#default Keyword Argument
# def fun_name (x=0,y=0,z=0):
#     print(f'{x,y,z}')
# fun_name(x=10,y=20)

# Variable Length Keyword Argument

# def fun_name( ** kwargs):
#     # print(kwargs)
#     # (print(type(kwargs)))
#     for k,v in kwargs.items():
#         print(f'{k} = {v}')
# var = eval(input("enter any dict: "))
# fun_name(** var)

# On the basis of argument and return
#type of functions

#1.) with argument and with return
# def show_detail (name):
#     return name
# x = input("enter your name: ")
# result = show_detail(x)
# print(result)

#2.) With argument and without return
# def details(name):
#     print('hello')
# details('abhi')

#3.) without argument with return
# def name():
#     return 'abhi'
# result = name()
# print(result)

#4.) without argument and without return
# def display():
#     print('hello')
# display()

# x,y = 10,20
# def add ():
#     p,q = 30,40
#     print(p,q)
#     print(x,y)
# add()
# print(x,y)
# print(p,q)

x,y = 10,20
def add():
    x= 39
    print(globals()['x']+x)
add()
print(x)