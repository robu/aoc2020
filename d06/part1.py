from functools import reduce

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

if __name__ == '__main__':
    answers = set() # one set of answers per group
    groups = [] # list of all groups' sets of answers
    for line in read_input():
        if len(line) == 0:
            groups.append(answers)
            answers = set()
        else:
            for c in line: answers.add(c)
    if (len(answers) > 0): groups.append(answers)
    count = reduce(lambda acc, elem: acc+elem, map(lambda x: len(x), groups), 0)
    print(count)
