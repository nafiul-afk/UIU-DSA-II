dpTable = [None] * 207

def factorial(n):
    if n<=1:
        return 1
    elif dpTable[n] != None:
        return dpTable[n]
    else:
        result = n * factorial(n-1)
        dpTable[n] = result
        return result

print(factorial(150))

print(dpTable)
