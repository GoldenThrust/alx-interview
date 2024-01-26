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

import re
import sys

total_size = 0
status_codes_count = {}
lines = 0


def parse_log(log):
    """
    Parse a log entry and update global variables.

    Args:
        log (str): Log entry string.

    Returns:
        bool: True if parsing is successful, False otherwise.
    """
    global total_size, lines
    try:
        pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' \
            r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

        match = re.match(pattern, log)
        if not match:
            raise Exception

        status_code, file_size = log.split()[-2:]
        status_code = int(status_code)

        total_size += int(file_size)

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        else:
            status_codes_count[status_code] = 1

        lines += 1

        return True
    except (ValueError, IndexError):
        return False


def print_log():
    """
    Prints the total file size and count of each HTTP status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        print("{}: {}".format(code, status_codes_count[code]))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            if not parse_log(line):
                continue

            if lines % 10 == 0:
                print_log()
    except KeyboardInterrupt:
        pass
    finally:
        print_log()
