# List Slicing

testList = [6, 9, 2, 1, 69, 21, "ELLOOO", "NO"]

# Return between range
print(testList[2:4])

# Return from index till end
print(testList[5:])

# Return from start till index
print(testList[:6])

# Adding a step to Slicing
print(testList[0:5:2])

# Reverse List using Slicing
print(testList[::-1])

# Using Slicing in Strings
testStr = "Elloooo"
print(testStr[::-1])

# Sets - Returns Distinct elements in lists
testSetList = [1, 1, 1, 1, 2, 2, 2, 5, 5, 5, 3, 8, 2,
               1, 7, 6, 4, 3, 5, 6, 7, 3, 2, 3, 5, 6, 2, 3, 9]
print(set(testSetList))

# Tuples - Immutable Objects (Can't be changed once created)
testTuple = (6, 9, "Ellooooooo", 2, 1, "Nooo", 69, 21)
print(testTuple)

# Dictionaries - Used to map key and values together (Sth SImilar to Hash map)
testDictionary = {0: "1st Value", 1: "2nd Value", "nums": 6921}
print(testDictionary["nums"])

# Add to dictionary
testDictionary["money"] = 10

# Replacing Values for a key in dictionary
testDictionary["nums"] = 2169

# Modify Values in Dictionary
testDictionary["money"] += 250

print(testDictionary)
