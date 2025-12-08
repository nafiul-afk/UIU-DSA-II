class Result:
    def __init__(self, summation, starting_index, ending_index):
        self.summation = summation
        self.starting_index = starting_index
        self.ending_index = ending_index
    
    def __str__(self):
        return f"Sum: {self.summation}, Index: ({self.starting_index}, {self.ending_index})"

def crossing_sum(lst, low, mid, high):
    # Left Subarray
    summation = lst[mid]
    left_summation = lst[mid]
    left_summation_index = mid
    
    for i in range(mid-1, low-1, -1):
        summation = summation + lst[i]
        if summation > left_summation:
            left_summation = summation
            left_summation_index = i
    
    summation = lst[mid+1]
    right_summation = lst[mid+1]
    right_summation_index = mid + 1
    
    for i in range(mid+2, high+1, 1):
        summation = summation + lst[i] 
        if summation > right_summation:
            right_summation = summation
            right_summation_index = i
    
    return Result(left_summation + right_summation, left_summation_index, right_summation_index)

def maximum_sum_subarray(lst, low, high):
    if low == high:
        return Result(lst[low], low, low)
    else:
        mid = (low + high) // 2
        
        left = maximum_sum_subarray(lst, low, mid)
        right = maximum_sum_subarray(lst, mid + 1, high)
        crossing = crossing_sum(lst, low, mid, high)
        
        if left.summation >= right.summation and left.summation >= crossing.summation:
            return left
        elif right.summation >= left.summation and right.summation >= crossing.summation:
            return right
        else:
            return crossing

result = maximum_sum_subarray([5, -6, 3, 7, -8, -1, 20, 9], 0, 7)

print(result)