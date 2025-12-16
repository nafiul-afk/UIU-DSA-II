from functools import cmp_to_key

def my_comparator(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


arr = [5, 2, 9, 1]
arr.sort(key=cmp_to_key(my_comparator))
print(arr)