a = int(input("enter your age : "))

if(a%2==0): #statement1 independent of other if
    print("a is even") 

if(a>=18):
    print("you are 18+ okay")

elif(a<=0):
    print("invalid age")

else :
    print("you are under 18")