# def outer(x):
#     def inner(p,q):
#         p = p+5
#         q= q+10
#         x(p,q)
#     return inner
# @outer
# def display(x,y):
#     print(x+y)
# display(10,20)

# def decorator (x):
#     def inner(p,q,r):
#         p= p+5
#         q = q+10
#         r= r+15
#         z= x(p,q,r)
#         return z
#     return inner
# @decorator
# def add(a,b,c):
#     return a+b+c
# res = add(2,4,6)
# print(res)

# def decorator (add):
#     def inner (p,q,r):
#         p = p*p
#         q = q*q
#         r = r**3
#         add(p,q,r)
#     return inner
# @decorator
# def add(x,y,z):
#     print(x+y+z)
# add(10,20,30)

def decorator(even_no):
    def inner(p,q,r):
        p= p-1
        even_no(p,q,r)
    return inner
@decorator
def even_no (start,stop,step):
    for i in range(start,stop+1,step):
        print(i)
s= 2
e = 101
r = 2
even_no(s,e,r)


    