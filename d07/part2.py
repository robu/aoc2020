from part1 import *

def count_bags_from(br_db, color):
    br = br_db[color]
    count = 1
    for (sub_color, sub_number) in br.can_contain.items():
        count += sub_number * count_bags_from(br_db, sub_color)
    return count

if __name__ == '__main__':
    rules = build_rule_dict()
    print(count_bags_from(rules, 'shiny gold') - 1)
