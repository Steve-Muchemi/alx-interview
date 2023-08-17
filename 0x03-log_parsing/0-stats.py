#!/usr/bin/python3
"""This file contains the solution to log parsing question"""


import sys
import datetime


total_file_size = 0
status_code_counts = {}

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        try:
            parts = line.strip().split()
            if len(parts) != 9:
                continue

            ip_address = parts[0]
            status_code = int(parts[7])
            file_size = int(parts[8])

            total_file_size += file_size
            status_code_counts[status_code] = status_code_counts.get(
                status_code, 0) + 1

            if line_number % 10 == 0:
                print("File size: {}".format(total_file_size))
                for code in sorted(status_code_counts):
                    print("{}: {}".format(code, status_code_counts[code]))
        except (ValueError, IndexError):
            continue
except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))
