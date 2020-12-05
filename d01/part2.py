from part1 import read_input, find_sum_pair

def find_sum_trio(target_value, arr):
    try:
        num1, num2 = find_sum_pair(target_value-arr[0], arr[0], arr[1:])
        return (arr[0], num1, num2)
    except:
        return find_sum_trio(target_value, arr[1:])

if __name__ == '__main__':
    in_data_vals = read_input()
    num1, num2, num3 = find_sum_trio(2020, in_data_vals)
    print("{0} * {1} * {2} = {3}".format(num1, num2, num3, num1*num2*num3))
