import re

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

class BagRule:
    def build(line):
        parts = re.match(r'^(.+) bags contain (.+)\.$', line)
        color = parts.group(1)
        br = BagRule(color)
        contains_lines = parts.group(2).split(',')
        for cl in contains_lines:
            try:
                cl_parts = re.match(r'( ?\d+) (.+) bags?', cl)
                cl_num = int(cl_parts.group(1))
                cl_color = cl_parts.group(2)
                br.add_container_color(cl_color, cl_num)
            except: pass
        return br

    def __init__(self, color):
        self.color = color
        self.can_contain = {}

    def add_container_color(self, color, number):
        self.can_contain[color] = number

    def __str__(self):
        return "{color}: {color_list}".format(color=self.color, color_list=list(self.can_contain))

def find_color(br_db, br, color):
    if br.color == color:
        return True
    else:
        l = list(br.can_contain)
        if color in l:
            return True
        else:
            for sub_color in l:
                sub_br = br_db[sub_color]
                if find_color(br_db, sub_br, color):
                    return True
            return False

def build_rule_dict():
    rules = {}
    for line in read_input():
        br = BagRule.build(line)
        rules[br.color] = br
    return rules

if __name__ == '__main__':
    rules = build_rule_dict()
    count = 0
    looking_for = 'shiny gold'
    rules.pop(looking_for) # dont include first level bag
    for color in list(rules):
        br = rules[color]
        if find_color(rules, br, looking_for):
            count += 1
    print(count)
