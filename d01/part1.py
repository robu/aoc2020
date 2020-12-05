def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return [int(s) for s in lines]

def find_sum_pair(target_value, arr):
    if len(arr) < 2: raise ValueError
    try:
        index = arr[1:].index(target_value - arr[0])
        return (arr[0], target_value - arr[0])
    except:
        return find_sum_pair(target_value, arr[1:])

if __name__ == '__main__':
    num1, num2 = find_sum_pair(2020, read_input())
    print("{0} * {1} = {2}".format(num1, num2, num1*num2))
