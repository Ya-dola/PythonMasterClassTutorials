# Using Lambda functions
print((lambda x, y: str(x**2) + " " + y)(4, "Ello"))

# Using Map (Recursive way of applying a function to a collection of data (list,set,dictionary) - most probably)
testSet = {1, 4, 9, 16, 25}

print(testSet)


def mapFunc(x):
    return x + 2


testMappedSet = set(map(mapFunc, testSet))

print(testMappedSet)
