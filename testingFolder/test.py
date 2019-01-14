print("Testing Print")
test = input("Who are you? ")
print("You are: " + test)

# If Function with converting from int to str
numTest = (3+4)
if (numTest == 7):
    print("Correct Answer: " + str(numTest))

# If with Else
if numTest == 4:
    print("In if statement")
else:
    print("In else statement")

# If with Elif and else
if numTest == 4:
    print("In if statement")
elif numTest == 7:
    print("In else if statement")
else:
    print("In else statement")

# While Loops
count = 0
while count < 3:
    print("Count Value is: " + str(count))
    count += 1

# While Loop with break
print("Running While Loop")
while True:
    user_input = input("Do you want to keep running this shit?: ")
    if user_input == "nah":
        break
    else:
        print("Sad Life, Maybe Next Time :P")
print("You saved your life!")

# List implementation
list1 = [6, 9, 2, 1, 69, 21, "ELLOOO", "NO"]
print("List - list1:")
print(list1)

if 69 in list1:
    print("Detected xD")

print("2nd Element in List: " + str(list1[1]))
print("Element Num of '21': " + str(list1.index(21)))

# Adding element to end of the list
list1.append("App")

# Adding element to list according to index specified
list1.insert(7, "YEA")

print("List - list1 (Mid Changes): ")
print(list1)

# Removing element in list
list1.remove("App")

print("List - list1 (After Changes): ")
print(list1)

# For Loops
print("List Content: ")
for i in list1:
    print(i)

print("For Loop with range defined: ")
for i in range(2, 5):
    print(i)


# Creating list from loop
list2 = [i for i in range(6, 9)]
print("List 2 : " + str(list2))
