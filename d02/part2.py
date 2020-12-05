from part1 import *

# this is for part 2
def valid_pw2(rule, pw):
    index1 = rule.range.start-1 # adjust for 1-based index
    index2 = rule.range.stop-2
    letter = rule.letter
    valid1 = len(pw) > index1 and pw[index1] == letter
    valid2 = len(pw) > index2 and pw[index2] == letter
    valid = valid1 != valid2
    return valid

if __name__ == '__main__':
    count = 0
    for line in read_input():
        if line_is_valid(line, valid_pw2):
            count = count + 1
    print(count)
