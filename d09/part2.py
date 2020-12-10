from part1 import *
from functools import reduce

def find_consecutive_sum(target, arr):
    for i in range(0, len(arr)):
        acc = 0
        ii = 0
        while acc < target and i+ii < len(arr):
            acc += arr[i+ii]
            ii += 1
        if acc == target:
            return arr[i:(i+ii)]
    return []

if __name__ == '__main__':
    nums = read_input()
    target = part1answer(nums)
    print("part1 target: {}".format(target))
    p2 = find_consecutive_sum(target, nums)
    #print("part2 arr:    {}".format(p2))
    #print("part2 sum:    {}".format(reduce(lambda acc, elem: acc+elem, p2, 0)))
    print("part2, min: {}, max: {}, minmax sum: {}".format(min(p2), max(p2), min(p2)+max(p2)))
