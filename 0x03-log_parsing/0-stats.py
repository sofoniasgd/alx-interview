#!/usr/bin/python3
""" Log parsing
    A script that reads stdin line by line and computes metrics:

    Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
            (see input format above)
        Number of lines by status code:
        possible status code:
            200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""

import signal
import sys


# define status codes with counters and a line counter
codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
         "405": 0, "500": 0}
file_size = 0
line_counter = 0


def print_report(code_dict, file_size):
    """ prints stat"""
    print("File size: {}".format(file_size))
    for key, value in code_dict.items():
        if value > 0:
            print("{}: {}".format(key, value))

try:
    for line in sys.stdin:
        # for every line either extract data or print if 10th line is reached
        word_list = line.split(" ")
        if len(word_list) == 9:
            # update status data
            file_size += int(word_list[-1])
            if word_list[-2] in codes.keys():
                codes[word_list[-2]] += 1
        line_counter += 1

        if line_counter == 10:
            # print_report
            print_report(codes, file_size)
            line_counter = 0
except Exception as err:
    pass
finally:
    # crrl-c pressed, print report and exit
    print_report(codes, file_size)
