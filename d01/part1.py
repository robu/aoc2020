def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return [int(s) for s in lines]

def find_sum_pair(target_value, term, arr):
    other_term = target_value - term
    try:
        index = arr.index(other_term)
        return (term, other_term)
    except:
        return find_sum_pair(target_value, arr[0], arr[1:])

if __name__ == '__main__':
    in_data_vals = read_input()
    num1, num2 = find_sum_pair(2020, in_data_vals[0], in_data_vals[1:])
    print("{0} * {1} = {2}".format(num1, num2, num1*num2))
