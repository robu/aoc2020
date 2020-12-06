import re

class Passport:
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    def __init__(self):
        self.fields = {}

    def keys(self):
        return list(self.fields)

    def parse_fields(self, line):
        pairs = line.split(' ')
        for pair_str in pairs:
            pair = pair_str.split(':')
            self.fields[pair[0]] = pair[1]

    def __validate_hgt(self, hgt):
        parts = re.match(r'^(\d{2,3})(cm|in)$', hgt)
        if parts:
            height = int(parts.group(1))
            if parts.group(2) == 'cm' and height in range(150,194): return True
            if parts.group(2) == 'in' and height in range(59,77): return True
        return False

    # this method if for part2, retrofitted into part1 code
    def validate_req_field_values(self):
        if not int(self.fields['byr']) in range(1920, 2003): return False
        if not int(self.fields['iyr']) in range(2010, 2021): return False
        if not int(self.fields['eyr']) in range(2020, 2031): return False
        if not self.__validate_hgt(self.fields['hgt']): return False
        if not re.match(r'^#[0-9a-f]{6}$', self.fields['hcl']): return False
        if not re.match(r'amb|blu|brn|gry|grn|hzl|oth', self.fields['ecl']): return False
        if not re.match(r'^[0-9]{9}$', self.fields['pid']): return False
        return True

    def has_required_fields(self):
        try:
            for rf in self.required_fields:
                if not (rf in self.keys()): return False
            return True
        except Exception as e:
            print("Exception: {0}".format(e))
            return False

    def validate(self):
        return self.has_required_fields() and self.validate_req_field_values()

    def to_s(self):
        status = 'NOT OK'
        if self.has_required_fields(): status = 'OK'
        return "{0} ({1})".format(self.keys(), status)

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

def read_passports():
    passports = []
    current_pp = Passport()
    for line in read_input():
        if len(line) == 0:
            passports.append(current_pp)
            current_pp = Passport()
        else:
            current_pp.parse_fields(line)
    return passports


if __name__ == '__main__':
    pps = read_passports()
    count = 0
    for pp in pps:
        if pp.has_required_fields(): count += 1
    print(count)
