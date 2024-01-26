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
    status_counts = {}
    for i, line in enumerate(sys.stdin, start=1):
        code = line.split(" ")
        try:
            total_size += int(code[-1])
            status = int(code[-2])
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1
        except (ValueError, IndexError):
            continue
        if i % 10 == 0:
            status_counts = dict(sorted(status_counts.items()))
            print("File size: {}".format(total_size))
            for key, val in status_counts.items():
                print("{}: {}".format(key, val))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in status_counts.items():
        print("{}: {}".format(key, val))
