def numberOfWays(current_position, destination):
    if current_position == destination:
        return 1
    elif current_position > destination:
        return 0
    else:
        waysForOneStepFromCurrent = numberOfWays(current_position+1, destination)
        waysForTwoStepFromCurrent = numberOfWays(current_position+2, destination)
        totalWays = waysForOneStepFromCurrent + waysForTwoStepFromCurrent
        return totalWays

print(numberOfWays(0, 100))