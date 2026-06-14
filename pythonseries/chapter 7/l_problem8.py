num = int(input("enter the number : "))

for i in range(1, num + 1):
    print(" "*(num-i), end="")
    print("*"*i,end="")
    print("\n")