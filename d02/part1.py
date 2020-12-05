import re

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

class Rule:
    def __init__(self, range, letter):
        self.range = range
        self.letter = letter

    def to_s(self): return "{0}-{1}: {2}".format(self.range.start, self.range.stop+1, self.letter)

    def validate(self, pw, validation_fun):
        return validation_fun(self, pw)

def build_rule(s):
    m = re.match(r'^(\d+)-(\d+) (\w)', s)
    return Rule(range(int(m.group(1)), int(m.group(2))+1), m.group(3))

def line_is_valid(line, valfun):
    rule = build_rule(line)
    pw = re.match(r'^.+: (\w+)$', line).group(1)
    return rule.validate(pw, valfun)

# this is for part 1
def valid_pw(rule, pw):
    return pw.count(rule.letter) in rule.range

if __name__ == '__main__':
    lines = read_input()
    count = 0
    for line in lines:
        if line_is_valid(line, valid_pw):
            count = count + 1
    print(count)
