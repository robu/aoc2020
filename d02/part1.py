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

    def valid_pw(self, pw):
#        print("validating '{0}' with {1}".format(pw, self.to_s()))
        return pw.count(self.letter) in self.range

def build_rule(s):
#    pattern = r'^(\d+)-(\d+) (\w)'
    m = re.match(r'^(\d+)-(\d+) (\w)', s)
    return Rule(range(int(m.group(1)), int(m.group(2))+1), m.group(3))

def line_is_valid(line):
    rule = build_rule(line)
    pw = re.match(r'^.+: (\w+)$', line).group(1)
    return rule.valid_pw(pw)

if __name__ == '__main__':
    lines = read_input()
    count = 0
    for line in lines:
        if line_is_valid(line):
            count = count + 1
    print(count)
