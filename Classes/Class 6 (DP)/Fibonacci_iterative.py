def fib(n):
    dpTable = [None] * (n+1)
    dpTable[0] = 0
    dpTable[1] = 1
    for i in range(2, n+1, 1):
        dpTable[i] = dpTable[i-1] + dpTable[i-2]
    
    print(dpTable)
    return dpTable[n]

print(fib(10))