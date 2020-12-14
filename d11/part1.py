def read_input():
    matrix = []
    with open('input.txt') as a_file:
        matrix = [list(l) for l in a_file.read().splitlines()]
    return matrix

class SeatLayout:
    def __init__(self, matrix):
        self.matrix = matrix

    def copy(self):
        other = []
        for line in self.matrix:
            other.append(line[:])
        return SeatLayout(other)

    def __str__(self):
        return "\n".join(["".join(line) for line in self.matrix])

    def equals(self, mtx2):
        return self.__str__() == mtx2.__str__()

    def adjacent_to(self, row, col):
        adjacents = []
        for r in range(max(0, row-1), min(len(self.matrix), row+2)):
            for c in range(max(0, col-1), min(len(self.matrix[row]), col+2)):
                if not (r == row and c == col):
                    adjacents.append(self.matrix[r][c])
        return adjacents

    def count_adjacent_with(self, row, col, char):
        return self.adjacent_to(row, col).count(char)

    def count_all_with(self, char):
        return self.__str__().count(char)

    def transformed(self):
        new = self.copy()
        for r in range(0, len(self.matrix)):
            for c in range(0, len(self.matrix[r])):
                if self.matrix[r][c] == 'L' and self.count_adjacent_with(r,c,'#') == 0:
                    new.matrix[r][c] = '#'
                elif self.matrix[r][c] == '#' and self.count_adjacent_with(r,c,'#') >= 4:
                    new.matrix[r][c] = 'L'
        return new

if __name__ == '__main__':
    lounge = SeatLayout(read_input())
    next = lounge.transformed()
    while not lounge.equals(next):
        lounge = next
        next = lounge.transformed()
    print(lounge.count_all_with('#'))
