# File Handling in Python

# Write a file
file = open("testFile.txt", "w")
file.write("Test File Written ! \n2nd line")
file.close()
print("File Written !")

# Read a file
readFile = open("testFile.txt", "r")
print(readFile.read())
readFile.close()

# Append a file
appendFile = open("testFile.txt", "a")
appendFile.write("\nAppended Text !")
appendFile.close()

appendFileRead = open("testFile.txt", "r")
print(appendFileRead.read())
appendFileRead.close()