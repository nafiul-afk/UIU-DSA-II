def printList(lst, n):
    if n == 1:
        print(lst[n-1], end = " ")
    else:
        printList(lst, n-1)
        print(lst[n-1], end = " ")
        
def printListReverse(lst, n):
    if n == 1:
        print(lst[n-1], end = " ")
    else:
        print(lst[n-1], end = " ")
        printListReverse(lst, n-1)
        

printListReverse([1, 2, 3, 4, 5, 6], 6)