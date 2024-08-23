#!/usr/bin/python3
"""0. Minimum Operations"""

import math
import primefac

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
    factors = [2]
    # print("factors", factors, type(factors))
    """
    if n <= 3:
        return
    for pf in range(3, math.floor(n / 2), 2):
        for i in range(2, pf):
            if pf % i == 0:
                break
            else:
                if pf not in factors:
                    factors.append(pf)
    """
    # print("factors list", primefac(n))
     pasted_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if can't be devided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 2

    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
