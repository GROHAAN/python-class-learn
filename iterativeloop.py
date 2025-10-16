# n = int(input("enter number"))
# i = 1
# sum = 1
# while (i<=n):
#     sum=sum*i
#     if i<=(n-1):
#         print(i,end='*')
#     else:
#         print(i,end='=')
#     i=i+1
# print(sum)

#* box 5*5
# n = int(input('enter any value'))
# i = 1
# while i<=n:
#     print(' # '*n)
#     i=i+1


# n = int(input('enter any value'))
# i = 1
# while i<=n:
#     print(' # '*i + ' '*(n-i))
#     i=i+1

# n = int(input('enter any value'))
# i = 1
# while i<=n:
#     print(' '*(n-i)+'* '* i )
#     i=i+1


# n = int(input('enter any value'))
# i = 0
# while i<n:
#     print(' '* i + ' *'*(n-i))
#     i=i+1


# n = int(input('enter any value'))
# i = 0
# while i < n:
#     print(' '*i + '* '*(n-i) )
#     i=i+1
# i=i-2
# while i>=0:
#     print(' '*i+'* '*(n-i) )
#     i=i-1

# n = int(input('enter any number : '))
# x = q = n

# sum = tg = 0
# while n>0:
#     tg +=1
#     n = n//10
# print(tg,n)
# print(f'total_digit of {x} is {tg}')
# while x>0:
#     last_digit = x%10
#     sum = sum + last_digit ** tg
#     x = x//10
# if q == sum:
#     print('armstrong')
# else:
#     print('not')

# ch = 'A'
# n = 10
# i = 1
# while i<=n:
#     print(ch,end=" ")
#     ch = chr(ord(ch)+1)
#     i = i+1

# By for loop
# i = 1
# ch = 'A'
# n = 5
# for i in range(n):
#     ch = 'A'
#     for i in range(n):
#         print(ch,end=' ')
#         ch = chr(ord(ch)+1)
#     print()

#by while loop
# n = 5
# i = 1

# while i<=n:    
#     j = 1
#     while j<=n:
#         print(j,end=' ')
#         j = j+1
#     print()
#     i = i+1

# 

# n = 5
# i = 1

# while i<=n:   
#     ch = 1 
#     j = 1
#     while j<=i:
#         print(ch,end=' ')
#         ch = ch+2
#         j = j+1
#     print()
#     i = i+1