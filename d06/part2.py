from part1 import *
import string

if __name__ == '__main__':
    answers = set(string.ascii_lowercase) # one set of answers per group
    groups = [] # list of all groups' sets of answers
    for line in read_input():
        if len(line) == 0:
            groups.append(answers)
            answers = set(string.ascii_lowercase)
        else:
            answers = answers.intersection(set(line))
    if (len(answers) < len(string.ascii_lowercase)): groups.append(answers)
    count = reduce(lambda acc, elem: acc+elem, map(lambda x: len(x), groups), 0)
    print(count)
