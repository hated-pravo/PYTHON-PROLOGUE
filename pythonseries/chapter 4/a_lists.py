friends = ["apple","aakash","rohan",7,0,6,False]
#lists can store any datatype
#unlike strings lists can mutable

print(friends[0])

l1="harry"
print(l1[2])

'''list methods '''

friends.append("harry")
print(friends)

l2 = [2,7,9,0,3,5,8,8]

l2.sort()
print(l2)

l2.insert(3,6) #add 6 at index 3
print(l2)

l2.pop(3) #removes element at index 3
print(l2)

l2.remove(8)
print(l2)