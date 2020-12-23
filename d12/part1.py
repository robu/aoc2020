import re

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

class Ferry:
    def __init__(self):
        self.direction = 'E'
        self.position_e = 0
        self.position_n = 0

    def __dir_to_degrees(self, dir):
        #print("__dir_to_degrees, {} => {}".format(dir,"ENWS".index(dir) * 90))
        return "ENWS".index(dir) * 90

    def __degrees_to_dir(self, deg):
        #print("__degrees_to_dir, {} => {}".format(deg,"ENWS"[int(((360+deg) / 90) % 4)]))
        return "ENWS"[int(((360+deg) / 90) % 4)]

    def move(self, instruction):
        parts = re.match(r'^([NSWELRF])(\d+)$', instruction)
        action = parts.group(1)
        value = int(parts.group(2))
        if action == 'F':
            action = self.direction

        if action == 'N':
            self.position_n += value
        elif action == 'S':
            self.position_n -= value
        elif action == 'E':
            self.position_e += value
        elif action == 'W':
            self.position_e -= value
        elif action == 'R':
            self.direction = self.__degrees_to_dir(self.__dir_to_degrees(self.direction) - value)
        elif action == 'L':
            self.direction = self.__degrees_to_dir(self.__dir_to_degrees(self.direction) + value)

    def manhattan_distance(self):
        return abs(self.position_e) + abs(self.position_n)

    def __str__(self):
        return "Facing {} at {}".format(self.direction, (self.position_e, self.position_n))

if __name__ == '__main__':
    lines = read_input()
    ferry = Ferry()
    for line in lines:
        ferry.move(line)
    print("After move, {}".format(ferry))
    print("Manhattan distance: {}".format(ferry.manhattan_distance()))
