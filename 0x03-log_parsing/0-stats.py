#!/usr/bin/python3
''' script that reads stdin line by line and computes metrics '''
import sys
import logging

logging.basicConfig(level=logging.ERROR)


if __name__ == "__main__":
    count = 0
    total_size = 0
    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    obj = {}

    try:
        for line in sys.stdin:
            lst = line.split(' ')
            if len(lst) < 2:
                continue

            try:
                count += 1
                status = int(lst[-2])
                size = int(lst[-1])
                total_size += size

                if status in codes:
                    if status in obj:
                        obj[status] += 1
                    else:
                        obj[status] = 1

                if count == 10:
                    count = 0
                    print('File size: {}'.format(total_size))
                    for el in sorted(obj.items()):
                        print('{}: {}'.format(el[0], el[1]))

            except ValueError:
                logging.error('Wrong format: {}'.format(line.strip()))
                continue

        print('File size: {}'.format(total_size))
        for el in sorted(obj.items()):
            print('{}: {}'.format(el[0], el[1]))

    except KeyboardInterrupt:
        print('File size: {}'.format(total_size))
        for el in sorted(obj.items()):
            print('{}: {}'.format(el[0], el[1]))