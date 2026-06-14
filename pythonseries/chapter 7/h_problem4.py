num = int(input("enter the number : "))

for i in range(2 , num , 1):
    if(num%i)==0:
        print("number is not prime")
        break

    else : 
        print("prime")
        break