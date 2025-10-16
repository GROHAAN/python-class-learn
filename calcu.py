while(True):
    print(" 1.add \n 2. sub \n 3.multi \n 4. division \n 5. exit")
    n = int(input("please select any of one option : "))
    if n in (1,2,3,4,5):
        if n in (1,2,3,4):
            if n==1:
                sum,l=0,[]
                n = int(input("enter how many no. you want to add"))     
                for i in range (1,n+1):
                    value = int(input(f"Enter {i} value : "))
                    l.append(value)
                    sum = sum+value
                print(f"sum of given value {i} is {sum}")
            if n==2:
                sub,l=0,[]
                n = int(input("enter how many no. you want to sub"))     
                for i in range (1,n+1):
                    value = int(input(f"Enter {i} value : "))
                    if i ==1:
                        sub = value
                        l.append(value)
                    else:
                        sub = sub-value
                        l.append(value)
                    print(f"sub of given value {i} is {sub}")
            if n==3:
                mul,l=1,[]
                n = int(input("enter how many no. you want to multiple"))     
                for i in range (1,n+1):
                    value = int(input(f"Enter {i} value : "))
                    l.append(value)
                    mul = mul*value
                print(f"mul of given value {i} is {mul}")
        else:
            break        
    else:
        print("please select valid option : ")