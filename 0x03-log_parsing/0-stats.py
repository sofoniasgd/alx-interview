#!/usr/bin/python3
""" Log parsing
    A script that reads stdin line by line and computes metrics:

    Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
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

# define report dictionary
# define status codes with counters and a line counter
codes = {"200":0, "301":0, "400":0, "401":0, "403":0, "404":0,"405":0, "500":0}
line_counter = 0;
report = {"File size": 0, "codes": codes}
print("report", report)


def print_report():
    """ Prints the report line """
    # clear the status code dict
    for key, value in codes.items():
        value = 0
    print("print")

def update_report(line):
    """Extracts Data from the log
        Line format:
            <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
            <file size>
    """
    # if the input is not the right format, exit function
    word_list = line.split(" ")
    if len(word_list) != 9:
        return

    print("update status {} file size{}#".format(word_list[-2], word_list[-1]))

# keyboard interrunpt(ctrl-c) handler function
def signal_handler(signal, frame):
    print("EXITING!")
    print_report()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    # for every line either extract data or print if 10th line
    if line_counter == 10:
        line_counter = 0
        print_report()
    else:
        line_counter += 1
        update_report(line)
