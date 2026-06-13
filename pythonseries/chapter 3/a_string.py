'''string slicing '''

name = "harry"

nameshort = name[0:3] #start from index 0 to the way till 3 (excluding 3)

print(nameshort)

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])

'''slicing with skip value'''

word = "amazing"
print(word[1:5:2])