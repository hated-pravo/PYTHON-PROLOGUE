marks = {   
    "harry": 100,
    "shubham": 56,
    "rohan": 26

}

print(marks , type(marks))

print(marks["harry"])

''' properties of dictionary
1) it is unorderd
2) it is mutable
3) it is indexed
4) cannot contain duplicate keys'''

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry":90 , "renuka": 67})

#print(marks["harry2"]) #gives an error
print(marks["renuka"]) 

print(marks.get("harry2")) #prints none