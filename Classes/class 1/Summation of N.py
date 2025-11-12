# iterative approach
def summation(n):
    total = 0
    for i in range(1, n+1, 1):
        total = total + i
    return total


# recursive approach
def summation(n):
    if n == 1:
        return 1
    else:
        friend = summation(n-1)
        total = friend + n
        return total


def printN(n):
    if n == 1:
        print(n, end = " ")
    else:
        print(n, end = " ")
        printN(n-1)
        

printN(100)