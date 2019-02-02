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

# Using Decorators (Wrapper Functions to provide extensibility)
# 1st way of doing it


def decorFunc(testfunc):
    def wrapperFunc():
        print("~~~~~~~~~~~~~~~~~~")
        testfunc()
        print("------------------")
    return wrapperFunc


def testfunc1():
    print("ELLOOOOOOOOOOOO")


def testfunc2():
    print("NOOOOOOOOOOOOOO")


decorated = decorFunc(testfunc1)

decorated()


decorated = decorFunc(testfunc2)

decorated()


# 2nd way of doing it

@decorFunc
def testfunc3():
    print("NICEEEEEEEEEEEE")


testfunc3()
