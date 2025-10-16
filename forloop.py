# s = {2,3,4,5,6,7,'python'}
# for i in s:
#     print(i)
# print('thanks',s)

# s = {'name': 'abhishek', 'age': 26, 'gender': 'male'}
# # for i,j in s.items():
# for i in s.values():
#     print(i)
# print('thanks',s)



n = int(input("enter any value : "))
#1.)   5x5 grid pattern
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print()

#2.)   left align traigle star pattern
# for i in range(1,n+1):
#     print('*'*i+ ' '*(n-1))

#3)   right align star pattern
# for i in range(1,n+1):
#     print(' '*(n-i)+ '*'*i )

#4)  traingle pattern
# for i in range(1,n+1):
#     print(' '*(n-i)+ ' *'*i )

#5)   right inverted star pattern
# for i in range(0,n+1):
#     print('*'*(n-i)+' '*i)

#6)   left inverted star pattern
# for i in range (0,n+1):
#     print(' '*i + '*'*(n-i))

#7)    inverted pyramid
# for i in range (0,n+1):
#     print(' '*i + '* '*(n-i))

#8)    right arrow star pattern
# for i in range(1,n+1):
#     print('*'*i + ' '*(n-i))
# for i in range(1,n+1):
#     print('*'*(n-i)+ ' '*i)

#9)    left arrow star pattern
# for i in range(1,n+1):
#     print(' '*(n-i)+ '*'*i)
# for i in range(1,n+1):
#     print(' '*i + '*'*(n-i))

#10)    Diamond star pattern
# for i in range(1,n+1):
#     print(' '*(n-i)+ '* '*i)
# for i in range(1,n+1):
#     print(' '*i + '* '*(n-i))

#11)     damru star pattern
# for i in range(0,n):
#     print(' '*i+ ' *'*(n-i))
# for i in range(2,n+1):
#     print(' '*(n-i)+ ' *'*i)

#12)     B structure star pattern

# for i in range(0,n):
#     print('*'*(n-i)+ ' '*i)
# for i in range(2,n+1):
#     print('*'*i + ' '*(n-i))

#13)    reverted  B structure star pattern
# for i in range(0,n):
#     print(' '*i + '*'*(n-i))
# for i in range(2,n+1):
#     print(' '*(n-i)+ '*'*i)

#15)   skew rectangle star pattern
# for i in range(1,n+1):
#     print('*'*i+ ' '*(n-i))
# for i in range(1,n+1):
#     print(' '*i + '*'*(n-i))

#16)  left skew rectangle star pattern

# for i in range(1,n+1):
#     print(' '*(n-i)+ '*'*i)
# for i in range(1,n+1):
#     print('*'*(n-i) + ' '*i)

