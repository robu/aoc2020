from functools import reduce

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines


if __name__ == '__main__':
    answers = set()
    groups = []
    count = 0
    for line in read_input():
        if len(line) == 0:
            count += len(answers)
            groups.append(answers)
            print("{0} ({1}): {2}".format(len(answers), count, answers))
            answers = set()
        for c in line:
            answers.add(c)

    print(count)
    c2 = reduce(lambda acc, elem: acc+elem, map(lambda x: len(x), groups), 0)
    print(c2)
