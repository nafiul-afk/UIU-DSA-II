def factorial(n):
    if n<0:
        return "[INVALID INPUT]"
    elif n==0:
        return 1
    else:
        friend = factorial(n-1)
        answer = friend * n
        return answer

print(factorial(n=45))