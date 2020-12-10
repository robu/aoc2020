def read_input():
    nums = []
    with open('input.txt') as a_file:
        nums = [int(a) for a in a_file.read().splitlines()]
    return nums.sorted()

if __name__ == '__main__':
    nums = read_input()
    target = max(nums) + 3
    base = 0
    max_delta = 3
    prev_jolt = base
    delta1_count = 0
    delta3_count = 0
    for n in nums:
        delta = n - prev_jolt
        if delta <= max_delta and n + max_delta <= target:
            if delta == 1: delta1_count += 1
            if delta == 3: delta3_count += 1
        prev_jolt = n
    delta3_count += 1 # add one for jolt to device

    print("d1: {}, d3: {}".format(delta1_count, delta3_count))
    print("product: {}".format(delta1_count * delta3_count))
