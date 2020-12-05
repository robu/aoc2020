from part1 import read_input, find_sum_pair

def find_sum_trio(target_value, arr):
    if len(arr) < 3: raise ValueError
    try:
        num1, num2 = find_sum_pair(target_value-arr[0], arr[1:])
        return (arr[0], num1, num2)
    except:
        return find_sum_trio(target_value, arr[1:])

if __name__ == '__main__':
    num1, num2, num3 = find_sum_trio(2020, read_input())
    print("{0} * {1} * {2} = {3}".format(num1, num2, num3, num1*num2*num3))
