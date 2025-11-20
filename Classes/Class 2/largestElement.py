def largestElement(lst, n):
    if n == 1:
        return lst[n-1]
    else:
        friend_answer = largestElement(lst, n-1)
        
        if friend_answer > lst[n-1]:
            return friend_answer
        else:
            return lst[n-1]

print(largestElement([1, 5, 3, 2, 8, 6], 6))