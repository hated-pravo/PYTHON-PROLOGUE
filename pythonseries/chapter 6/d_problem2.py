marks1 = int(input("enter marks 1 : "))
marks2 = int(input("enter marks 2 : "))
marks3 = int(input("enter marks 3 : "))

total_percen = (marks1 + marks2 + marks3)/3

if(total_percen >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("you are pass" , total_percen)

else:
    print("you are fail" , total_percen)