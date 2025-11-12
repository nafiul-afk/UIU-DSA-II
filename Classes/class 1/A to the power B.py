def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

def power_e(a, b):
    if b == 0:
        return 1
    elif b%2 == 0:
        # b is even
        answer = power_e(a, b//2)
        return answer * answer
    else:
        # b is odd
        return a * power_e(a, b-1)

print(power(5, 3))
