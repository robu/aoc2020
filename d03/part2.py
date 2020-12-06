from part1 import *

class Part2Slope(Part1Slope):
    def __init__(self, filename):
        super().__init__(filename)

    def count_trees_on_run(self, delta_lines, delta_cols):
        self.restart_pos()
        self.set_deltas(delta_lines, delta_cols)
        return self.count_trees()

if __name__ == '__main__':
    slope = Part2Slope('input.txt')
    list = []
    list.append(slope.count_trees_on_run(1,1))
    list.append(slope.count_trees_on_run(1,3))
    list.append(slope.count_trees_on_run(1,5))
    list.append(slope.count_trees_on_run(1,7))
    list.append(slope.count_trees_on_run(2,1))
    print(list[0]*list[1]*list[2]*list[3]*list[4])
