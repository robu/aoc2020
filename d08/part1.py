import re

def read_input():
    lines = []
    with open('input.txt') as a_file:
        lines = a_file.read().splitlines()
    return lines

class CPU:
    def __init__(self, lines):
        self.reset(lines)

    def reset(self, lines):
        self.accumulator = 0
        self.memory = []
        self.run_history = []
        self.pointer = 0
        for line in lines:
            self.add_line_to_memory(line)

    def add_line_to_memory(self, line):
        parts = re.match(r'(acc|jmp|nop) ([\-\+]\d+)', line)
        operation = parts.group(1)
        argument = int(parts.group(2))
        self.memory.append((operation, argument))
        self.run_history.append(False)

    def run_until_loop(self):
        while not (self.pointer >= len(self.memory) or self.run_history[self.pointer]):
            operation, argument = self.memory[self.pointer]
            self.run_history[self.pointer] = True
            if operation == 'acc':
                self.accumulator += argument
                self.pointer += 1
            elif operation == 'jmp':
                self.pointer += argument
            else:
                self.pointer += 1
        return self.pointer >= len(self.memory) # true if ran all the way to the end

    def __str(self, addr):
        return "{}: {} {:+d}".format(addr, self.memory[addr][0], self.memory[addr][1])

    def __str__(self):
        return "\n".join([self.__str(addr) for addr in range(0,len(self.memory))])

if __name__ == '__main__':
    cpu = CPU(read_input())
    cpu.run_until_loop()
    print(cpu.accumulator)
