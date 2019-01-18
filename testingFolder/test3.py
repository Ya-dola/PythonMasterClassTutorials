# File Handling in Python

# Write a file
file = open("testFile.txt", "w")
file.write("Test File Written ! \n2nd line")
file.close()
print("File Written !")

# Read a file
readFile = open("testFile.txt", "r")
print(readFile.read())
