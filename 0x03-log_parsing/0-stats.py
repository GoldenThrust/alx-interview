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
    total_size = 0
    status_codes_count = {}
    for i, line in enumerate(sys.stdin, start=1):
        status_code, file_size = line.split(' ')[-2:]
        try:
            status_code = int(status_code)

            total_size += int(file_size)

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
            else:
                status_codes_count[status_code] = 1

        except (ValueError, IndexError):
            continue

        status_codes_count = dict(sorted(status_codes_count.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in status_codes_count.items():
                print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in status_codes_count.items():
        print("{}: {}".format(key, value))
