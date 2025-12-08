def min_max_find(lst, low, high):
    if low == high:
        return [lst[low], lst[low]]
    elif low+1 == high:
        if lst[low]<lst[high]:
            return [lst[low], lst[high]]
        else:
            return [lst[high], lst[low]]
    else:
        mid = (low + high) // 2
        left = min_max_find(lst, low, mid)
        right = min_max_find(lst, mid+1, high)
        
        final_answer = []
        # min comparison
        if left[0]<right[0]:
            final_answer.append(left[0])
        else:
            final_answer.append(right[0])
        
        # max comparison
        if left[1]>right[1]:
            final_answer.append(left[1])
        else:
            final_answer.append(right[1])
        
        return final_answer

print(min_max_find([5, 6, 3, 2, 8, 1, 9, 7], 0, 7))