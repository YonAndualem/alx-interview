#!/usr/bin/python3

"""
Module that performs log parsing from stdin
"""

import re
import sys

counter = 0
file_size = 0
statusC_counter = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_codes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print(f"File size: {file_s}")
    for key in sorted(dict.keys()):
        if statusC_counter[key] != 0:
            print(f"{key}: {dict[key]}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                print_codes(statusC_counter, file_size)
            counter += 1
            try:
                statusC, f_size = map(int, statusC_and_file_s.split())
                if statusC in statusC_counter:
                    statusC_counter[statusC] += 1
                file_size += f_size
            except:
                pass
        print_codes(statusC_counter, file_size)
    except KeyboardInterrupt:
        print_codes(statusC_counter, file_size)
        raise
