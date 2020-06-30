def dummyFunction (a : int=6, b : int=2):
    return  a *b


print (dummyFunction(b=6))

def unlimitedArguments(*args):
    sum =0
    for x in args:
        sum +=x
    return  sum

print(unlimitedArguments(2,3,5))

