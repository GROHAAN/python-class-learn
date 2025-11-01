#map() function


# l = [1,2,3,4,5]
# def square(n):
#     return n*n
# result = map(square,l)
# print(result)
# print(tuple(result))

# l1 = [1,3,5,7]
# l2 = [1,2,3]
# l3 = [1,2,3,4,5,6,7]
# def add (x,y,z):
#     return x+y+z
# result = list(map(add,l1,l2,l3))
# print(result)

#2,) filter() function
# l = [1,2,3,4,5,6,6]
# def even(n):
#     if n%2==0:
#         return n
# result = list(filter(even,l))
# print(result)

# l = [1,2,3,4,5,6]
# def even (n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# result = list(map(even,l))
# print(result)

#3.) reduce() function
from functools import reduce
# import functools

# l = [1,2,3,4,5]
# def add (x,y):
#     return x+y
# result = functools.reduce(add,l)
# print(result)

# l = [10,20,5,58,47,36,37]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# result = reduce(max,l)
# print(result)