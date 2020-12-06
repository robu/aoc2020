class Slope:
    def __init__(self, filename):
        self.read_input(filename)
        self.pos_line = 0
        self.pos_col = 0

    def read_input(self, filename):
        self.lines = []
        with open('input.txt') as a_file:
            self.lines = a_file.read().splitlines()
        return self.lines

    def content_at(self, line, col):
        return self.lines[line][col % len(self.lines[line])]

    def current_content(self):
        return self.content_at(self.pos_line, self.pos_col)

    def move_pos(self, lines, cols):
        self.pos_line += lines
        self.pos_col += cols

    def slope_done(self):
        return self.pos_line >= len(self.lines)

class Part1Slope(Slope):
    def __init__(self, filename, delta_lines, delta_cols):
        super().__init__(filename)
        self.delta_lines = delta_lines
        self.delta_cols = delta_cols

    def move(self):
        l = self.pos_line
        c = self.pos_col
        self.move_pos(self.delta_lines, self.delta_cols)

    def current_is_tree(self): return self.current_content() == '#'

    def count_trees(self):
        count = 0
        while not self.slope_done():
            if self.current_is_tree(): count += 1
            self.move()
        return count

if __name__ == '__main__':
    slope = Part1Slope('input.txt', 1, 3)
    print(slope.count_trees())
