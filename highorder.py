l = [1,2,3,4,5]
def square(n):
    return n*n
result = map(square,l)
print(result)
print(tuple(result))