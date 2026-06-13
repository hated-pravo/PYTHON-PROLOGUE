grade = int(input("enter your grade : "))

if( grade <= 100 and grade >=90):
    print("excelent")

elif(grade < 90 and grade>=80) :
    print("A GRADE")

elif(grade < 80 and grade>=70):
    print("B GRADE")
elif(grade<= 70 and grade >=60):
    print("C GRADE")

elif(grade<60 and grade>=50):
    print("D GRADE")
else:
    print("you are fail")