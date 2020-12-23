from part1 import *

class Ferry2:
    def __init__(self):
        self.position_e = 0
        self.position_n = 0
        self.set_waypoint(0,0)

    def __move_waypoint(self, action, value):
        if action == 'N':
            self.waypoint_n += value
        elif action == 'S':
            self.waypoint_n -= value
        elif action == 'E':
            self.waypoint_e += value
        elif action == 'W':
            self.waypoint_e -= value

    def __move_ferry(self, value):
        for i in range(0, value):
            self.position_n += self.waypoint_n
            self.position_e += self.waypoint_e

    def set_waypoint(self, e, n):
        self.waypoint_e = e
        self.waypoint_n = n

    def __action_value(self, instruction):
        parts = re.match(r'^([NSWELRF])(\d+)$', instruction)
        action = parts.group(1)
        value = int(parts.group(2))
        return (action, value)

    def __turn_wp_right(self):
        e, n = self.waypoint_e, self.waypoint_n
        self.waypoint_e = n
        self.waypoint_n = -e

    def __turn_wp_left(self):
        e, n = self.waypoint_e, self.waypoint_n
        self.waypoint_e = -n
        self.waypoint_n = e

    def move(self, instruction):
        action, value = self.__action_value(instruction)
        if action in "ENWS":
            return self.__move_waypoint(action, value)
        elif action == 'F':
            self.__move_ferry(value)
        elif action == 'R':
            for n in range(0, int(value/90)):
                self.__turn_wp_right()
        elif action == 'L':
            for n in range(0, int(value/90)):
                self.__turn_wp_left()

    def __str__(self):
        return "Position at {} with waypoint at {}".format((self.position_e, self.position_n), (self.waypoint_e, self.waypoint_n))

    def manhattan_distance(self):
        return abs(self.position_e) + abs(self.position_n)

if __name__ == '__main__':
    lines = read_input()
    ferry = Ferry2()
    ferry.set_waypoint(10, 1)
    for line in lines:
        ferry.move(line)
    print(ferry)
    print("Manhattan distance: {}".format(ferry.manhattan_distance()))
