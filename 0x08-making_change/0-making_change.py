#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort the coins in descending order
    total_coins = 0

    try:
        for coin in coins:
            while total >= coin:
                total -= coin
                total_coins += 1

        if total == 0:
            return total_coins
        else:
            return -1
    except IndexError:
        return -1
