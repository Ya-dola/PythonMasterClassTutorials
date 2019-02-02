# Using Lambda functions
print((lambda x, y: str(x**2) + " " + y)(4, "Ello"))

# Using Map (Recursive way of applying a function to a collection of data (list,set,dictionary))
testSet = {1, 4, 9, 16, 25}

print(testSet)


def mapFunc(x):
    return x + 2


testMappedSet = set(map(mapFunc, testSet))

print(testMappedSet)

# Using Filters (Filters Data out that meet a certain criteria)
testFilteredSet = set(filter(lambda x: x % 2 == 0, testSet))

print(testFilteredSet)

# Using Generator Functions (Good way to iterate through function without taking up memory)


def genFunc():
    for i in range(4):
        yield i


for i in genFunc():
    print(i)
