a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))
d = int(input("enter the 4th number : "))

if(a>=b and a>=c and a>=d):
    print("the greatest number you entered is : ",a)

elif(b>=a and b >= c and b >=d):
    print("the greatest number you entered is : ",b)

elif(c>=a and c >= b and c >=d):
    print("the greatest number you entered is : ",c)

else :
    print("the greatest number you entered is : ",d)




