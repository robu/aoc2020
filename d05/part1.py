import re

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

class RangeFinder:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def to_s(self): return "{0}-{1}".format(self.lower, self.upper)

    def __half_delta(self): return int(self.delta() / 2)

    def delta(self): return self.upper - self.lower + 1

    def front(self):
        return RangeFinder(self.lower, self.lower + self.__half_delta()-1)

    def back(self):
        return RangeFinder(self.lower + self.__half_delta(), self.upper)


def seat_from_pass(line):
    parts = re.match(r'([FB]{7})([LR]{3})', line)
    row = RangeFinder(0,127)
    for c in parts.group(1):
        if c == 'F':
            row = row.front()
        else:
            row = row.back()
    seat = RangeFinder(0,7)
    for c in parts.group(2):
        if c == 'L':
            seat = seat.front()
        else:
            seat = seat.back()
    return (row.lower, seat.lower)

if __name__ == '__main__':
    highest_id = -1
    for line in read_input():
        row, seat = seat_from_pass(line)
        seat_id = row * 8 + seat
        # print("({0}, {1}), {2} : {3}".format(row, seat, seat_id, line))
        if seat_id > highest_id: highest_id = seat_id
    print(highest_id)
