dpTable = [None] * 20
parent = [None] * 20

import math

def coin_change(amount, coins):
    if amount == 0:
        return 0
    elif dpTable[amount] != None:
        return dpTable[amount]
    else:
        answer = math.inf
        which_coin = math.inf
        
        for coin in coins:
            if amount < coin:
                continue
            else:
                result = 1 + coin_change(amount - coin, coins)
                if result < answer:
                    answer = result
                    which_coin = coin
        
        dpTable[amount] = answer
        parent[amount] = which_coin
        return answer
    
result = coin_change(10, [1, 5, 6, 8])
print(result)

print(dpTable)
print(parent)
            
