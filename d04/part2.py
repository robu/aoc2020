from part1 import *


if __name__ == '__main__':
    pps = read_passports()
    count = 0
    for pp in pps:
        if pp.validate(): count += 1
    print(count)
