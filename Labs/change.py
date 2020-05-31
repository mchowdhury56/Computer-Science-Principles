from cs115 import*

def change(amount, coins):
    ''' returns the least number of coins needed to make an amount based on a
        list of coin values'''
    if amount == 0: #if the amount needed is 0
        return 0
    elif coins == []: #if an amount is needed but there's no coin values (no solution)
        return float("inf")
    else: #we have an amount and list of coin values
        if coins[len(coins) - 1] > amount:
            return change(amount,coins[0:len(coins) - 1])
        else:
            use = 1 + change(amount-coins[len(coins) - 1], coins)
            lose = change(amount,coins[0:len(coins) - 1])
            return min(use,lose)
