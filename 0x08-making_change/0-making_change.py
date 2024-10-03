#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    """determines the fewest number of coins needed to meet a given amount
        Args:
            coints (list) list of different coin values
            total (int) the total amount
        Returns:
            fewest number of coins needed to meet total
    """
    # sort the coin value list Descending
    coins.sort(reverse=True)
    total = total
    # Algorithm
    # number of coins is found by starting division by the
    # largest value, storing quotient(number of coins of the current value)
    # and then dividing the remainder by the next smaller value
    # if there exists a remainder after the last diviion(smallest coin value)
    # then theres no solution
    amount = 0
    if not coins or total < coins[-1]:
        return -1
    for value in coins:
        remainder = total % value
        if coins[-1] == value and remainder != 0:
            return -1
        amount += total // value
        total = remainder
    return amount
