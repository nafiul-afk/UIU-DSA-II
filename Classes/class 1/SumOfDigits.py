def sumOfDigits(n):
    if n<10:
        return n
    else:
        my_digit = n%10
        friend_answer = sumOfDigits(n//10)
        final_answer = friend_answer + my_digit
        return final_answer

def countOfDigits(n):
    if n<10:
        return 1
    else:
        my_answer = 1
        friend_answer = countOfDigits(n//10)
        final_answer = friend_answer + my_answer
        return final_answer

print(sumOfDigits(1247))