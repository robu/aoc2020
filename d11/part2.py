from part1 import *

class SeatLayout2(SeatLayout):
    def __init__(self, matrix):
        super().__init__(matrix)

    # returns '.' if nothing else is seen in the direction, otherwise the first non-'.' char seen
    def viewable_in_direction(self, row, col, delta_row, delta_col):
        rmax = len(self.matrix)
        cmax = len(self.matrix[0]) # assume equal num of cols in all rows
        row += delta_row
        col += delta_col
        while row >= 0 and row < rmax and col >= 0 and col < cmax:
            if self.matrix[row][col] != '.': return self.matrix[row][col]
            row += delta_row
            col += delta_col
        return '.'

    # need to override to return the derived type
    def copy(self):
        other = []
        for line in self.matrix:
            other.append(line[:])
        return SeatLayout2(other)

    def visible_in_all_directions(self, row, col):
        viewable = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if not (dr==0 and dc==0):
                    v = self.viewable_in_direction(row, col, dr, dc)
                    if v != '.':
                        viewable.append(v)
        return viewable

    def count_visible_with(self, row, col, char):
        return self.visible_in_all_directions(row, col).count(char)

    def transformed2(self):
        new = self.copy()
        for r in range(0, len(self.matrix)):
            for c in range(0, len(self.matrix[r])):
                if self.matrix[r][c] == 'L' and self.count_visible_with(r,c,'#') == 0:
                    new.matrix[r][c] = '#'
                elif self.matrix[r][c] == '#' and self.count_visible_with(r,c,'#') >= 5:
                    new.matrix[r][c] = 'L'
        return new


if __name__ == '__main__':
    lounge = SeatLayout2(read_input())
    next = lounge.transformed2()
    while not lounge.equals(next):
        lounge = next
        next = lounge.transformed2()
    print(lounge.count_all_with('#'))
