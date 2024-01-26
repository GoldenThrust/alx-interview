#!/usr/bin/python3
"""
Log Parsing Script

This script parses log files containing entries with a specific format
and extracts relevant information, such as total file size and counts of each
HTTP status code.

Usage:
    ./log_parser.py < logfile.txt
    - Reads log entries from standard input (stdin).

Log Entry Format:
    Each log entry is expected to follow the format:
    <IP Address> - [<Timestamp>] "GET /projects/260 HTTP/1.1"
    <HTTP Status Code> <File Size>

Example Log Entry:
    192.168.1.1 - [2024-01-26 12:34:56] "GET /projects/260 HTTP/1.1" 200 1024

"""

import sys


try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split(" ")
        try:
            total_size += int(parts[-1])
            status = int(parts[-2])
            if status not in my_dict:
                my_dict[status] = 1
            else:
                my_dict[status] += 1
        except (ValueError, IndexError):
            continue
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
