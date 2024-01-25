#!/usr/bin/python3
""" Log Parsing """
import re
import sys

total_size = 0
status_codes_count = {}
lines = 0

try:
    for line in sys.stdin:
        status_code, file_size = re.split(r'\ ', line)[-2:]

        file_size = int(file_size)
        status_code = int(status_code)

        total_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        else:
            status_codes_count[status_code] = 1

        lines += 1

        if lines % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes_count.keys()):
                print("{}: {}".format(code, status_codes_count[code]))
    print("{}: {}".format(code, status_codes_count[code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        print("{}: {}".format(code, status_codes_count[code]))

    sys.exit(0)
