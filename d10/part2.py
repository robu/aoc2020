from part1 import read_input

def extract_max_delta(arr, base, delta):
    subarr = []
    for num in arr:
        if num <= base+delta:
            subarr.append(num)
        else:
            return subarr
    return subarr

def count_combos(arr, target, delta, history=set()):
    first = arr[0]
    if first in history: return 0 # already been counted
    subarr = extract_max_delta(arr[1:], first, delta)
    #print("subarr: ({}) {}".format(first, subarr))
    count = 1 if len(subarr) > 0 else 0
    for subindex in range(0, len(subarr)): # [(1), 2, 5, 6]
        count += count_combos(arr[(1+subindex):], target, delta, history)
    history.add(first)
    #history.clear()
    return count

if __name__ == '__main__':
    nums = read_input()
    delta = 3
    target = max(nums) + delta
    print("{}".format(count_combos(nums, target, delta)-2))
