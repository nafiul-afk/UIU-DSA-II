def numberOfWaysAmount(current_amount, destination_amount):
    if current_amount == destination_amount:
        return 1
    elif current_amount > destination_amount:
        return 0
    else:
        waysForOne = numberOfWaysAmount(current_amount + 1, destination_amount)
        waysForTwo = numberOfWaysAmount(current_amount + 2, destination_amount)
        waysForFive = numberOfWaysAmount(current_amount + 5, destination_amount)
        
        totalWays = waysForOne + waysForTwo + waysForFive
        
        return totalWays


print(numberOfWaysAmount(0, 3))