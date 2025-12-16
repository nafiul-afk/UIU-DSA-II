dpTable = [None]*101

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dpTable[n] != None:
        return dpTable[n]
    else:
        result = fib(n-1) + fib(n-2)
        dpTable[n] = result
        return result

print(fib(10))

print(dpTable)

print(fib(11))

print(dpTable)
