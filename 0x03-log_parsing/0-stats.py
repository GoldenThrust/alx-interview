#!/usr/bin/python3
""" Log Parsing """
import re
import sys

total_size = 0
status_codes_count = {}
lines = 0


def parse_log(log):
    global total_size, lines
    try:
        pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' \
            r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

        match = re.match(pattern, log)
        if not match:
            raise Exception

        status_code, file_size = re.split(r'\ ', log)[-2:]
        file_size = int(file_size)
        status_code = int(status_code)

        total_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        else:
            status_codes_count[status_code] = 1

        lines += 1

        return True
    except Exception as e:
        print(e)
        return False


def print_log():
    """Prints the total file size and count of each HTTP status code."""
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

        print_log()
    except KeyboardInterrupt:
        print_log()
