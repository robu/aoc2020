from part1 import *

def seat_id_from_pass(line):
    row, seat = seat_from_pass(line)
    return row * 8 + seat

if __name__ == '__main__':
    id_tracker = []
    for line in read_input():
        id_tracker.append(seat_id_from_pass(line))
    id_tracker.sort()
    prev_id = id_tracker[0]
    for i in id_tracker[1:]:
        if not i == prev_id + 1:
            print(prev_id + 1)
        prev_id = i
