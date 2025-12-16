import math

def coin_change(amount, coins):
    if amount == 0:
        return 0
    else:
        answer = math.inf
        
        for coin in coins:
            if amount < coin:
                continue
            else:
                result = 1 + coin_change(amount - coin, coins)
                if result < answer:
                    answer = result
        
        return answer
    
result = coin_change(10, [1, 5, 6, 8])
print(result)
            