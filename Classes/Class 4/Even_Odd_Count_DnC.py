def even_odd_count(lst, low, high):
    if low == high:
        if lst[low]%2 == 0:
            return [1, 0]
        else:
            return [0, 1]
    else:
        mid = (low + high) // 2
        left = even_odd_count(lst, low, mid)
        right = even_odd_count(lst, mid + 1, high)
        
        return [left[0]+right[0], left[1]+right[1]]

print(even_odd_count([5, 6, 3, 2, 8, 1, 9, 7], 0, 7))