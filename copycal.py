while(True):
    print(" 1.add \n 2. sub \n 3.multi \n 4. division \n 5. exit")
    n = int(input("please select any of one option : "))
    if n in (1, 2, 3, 4, 5):
        if n in (1, 2, 3, 4):
            if n==1:
                sum=0
                li = []
                n = int(input('How Many Number You Want to Add: '))
                for i in range(1,n+1):
                    val = int(input(f'enter {i} number: '))
                    li.append(val)
                    sum = sum+val
                print(f"sum of given value {i} is {sum}")



    else:
        print('please enter any valid option:')