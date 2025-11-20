def smallestLargestElement(lst, n):
    if n == 1:
        return (lst[n-1], lst[n-1])
    else:
        friend_answer = smallestLargestElement(lst, n-1)
        
        if friend_answer[0] > lst[n-1]:
            return (lst[n-1], friend_answer[1])
        elif friend_answer[1] < lst[n-1]:
            return (friend_answer[0], lst[n-1])
        else:
            return friend_answer

print(smallestLargestElement([1, 5, 3, 2, 8, 6], 6))

