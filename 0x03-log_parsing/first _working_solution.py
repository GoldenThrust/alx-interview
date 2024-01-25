#!/usr/bin/python3
""" Log Parsing """
import sys
import signal
import re

i = 1
status_codes_count = {}
total_files = 0
line = [None]


def parse_log():
    print(f'File size: {total_files}')
    sorted_data = dict(sorted(status_codes_count.items()))

    for key, values in sorted_data.items():
        print(f'{key}: {values}')


def sigint_handler(signal, frame):
    parse_log()
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)

while line[0] != '':
    line = sys.stdin.readline()
    line = re.split(r'\ ', line)[-2:]

    if line[0] != '':
        if line[0] in status_codes_count:
            status_codes_count[line[0]] += 1
        else:
            status_codes_count[line[0]] = 1

        total_files += int(line[1])

    if i % 10 == 0:
        parse_log()

    i += 1
