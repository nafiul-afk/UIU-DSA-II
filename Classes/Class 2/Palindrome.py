def isPalindrome(string, low, high):
    if low >= high:
        return True
    else:
        friend_answer = isPalindrome(string, low + 1, high - 1)
        my_answer = True
        
        if string[low] != string[high]:
            my_answer = False
        
        final_answer = (friend_answer and my_answer)
        return final_answer
        

print(isPalindrome("novovon", 0, 6))