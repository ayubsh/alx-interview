#!/usr/bin/env python3
"""Log parsing"""
import sys
import signal


def print_stats(file_size, status_codes):
    """prints the stats to the stdout
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """handles singnals
    """
    print_stats(file_size, status_codes)
    sys.exit(0)


file_size = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split(" ")
        if len(parts) < 9:
            continue
        size = int(parts[-1])
        code = parts[-2]
        if code in status_codes:
            status_codes[code] += 1
            file_size += size
            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
    except ValueError:
        continue

print_stats(file_size, status_codes)
