#!/usr/bin/python3
"""
Main file for testing
"""
import sys

minOperations = __import__('0-minoperations').minOperations

for i in range(1, len(sys.argv)):
    print("prime factors of {} are: ||{}||".format(sys.argv[i], minOperations(int(sys.argv[i]))))
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

