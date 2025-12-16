import math

def coin_change_iterative(amount, coins):
    dpTable = [None] * (amount+1)
    parent = [None] * (amount+1)
    
    dpTable[0] = 0
    parent[0] = 0
    
    for i in range(1, amount+1, 1):
        
        answer = math.inf
        which_coin = math.inf
        
        for coin in coins:
            if coin>i:
                continue
            else:
                result = 1 + dpTable[i-coin]
                if result < answer:
                    answer = result
                    which_coin = coin
        
        dpTable[i] = answer
        parent[i] = which_coin
    
    
    print("DP Table " , dpTable)
    print("Path ", parent)
    
    return dpTable[amount]


result = coin_change_iterative(10, [1, 5, 6, 8])
print(result)