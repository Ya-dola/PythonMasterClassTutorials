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
