class Passport:
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    optional_fields = ['cid']

    def __init__(self):
        self.fields = {}

    def keys(self):
        return list(self.fields)

    def parse_fields(self, line):
        pairs = line.split(' ')
        for pair_str in pairs:
            pair = pair_str.split(':')
            self.fields[pair[0]] = pair[1]

    def has_required_fields(self):
        try:
            for rf in self.required_fields:
                if not (rf in self.keys()): return False
            return True
        except Exception as e:
            print("Exception: {0}".format(e))
            return False

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
