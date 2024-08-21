#!/usr/bin/python3
"""0. Minimum Operations"""

import math

def minOperations(n):
    """In a text file, there is a single character H.
        Your text editor can execute only two operations in this file:
            Copy All and Paste. 
        Given a number n, this method calculates the fewest number of 
        operations needed to result in exactly n H characters in the file.
        Args:
            n: int
        Returns: int
        Example:
            n = 9
            H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
            Paste => HHHHHH => Paste => HHHHHHHHH
            Number of operations=6
    """
    # solution #1 using prime facorization
    # the summ of all the prime factors is the same as the minimum number
    # of operations to get 'n' number of H characters
    sum_of_pime_factors = []
    factors = [1,2]
    for pf in range(3, math.floor(n / 2), 2):
        factors.append(pf)
    print("factors list", factors)
    while True:
        for pf in factors:

