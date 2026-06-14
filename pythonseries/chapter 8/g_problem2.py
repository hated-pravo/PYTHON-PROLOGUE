def therm(c):
    f = ((9*c)/5) + 32
    return f

c = int(input("enter the temp in celsius : "))
 
print(f"conversion of {c} celsius to {therm(c)} farehneit ")