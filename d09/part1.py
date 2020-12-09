from functools import reduce

def read_input():
    nums = []
    with open('input.txt') as a_file:
        nums = [int(a) for a in a_file.read().splitlines()]
    return nums

def has_sum_of_2(target, arr):
    if len(arr) < 2: return False
    first = arr[0]
    term = target - first
    try:
        i = arr[1:].index(term)
        return True
    except:
        return has_sum_of_2(target, arr[1:])

def part1answer(nums):
    window_size = 25
    for i in range(window_size, len(nums)):
        if not has_sum_of_2(nums[i], nums[i-window_size : i]):
            return nums[i]


if __name__ == '__main__':
    nums = read_input()
    print(part1answer(nums))
