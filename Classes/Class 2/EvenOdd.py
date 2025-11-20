def printEven(n):
    if n<1:
        return
    else:
        printEven(n-1)
        
        if n%2 == 0:
            print(n, end = " ")


printEven(0)