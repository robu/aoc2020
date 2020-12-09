from part1 import *

class CPU2(CPU):
    def __init__(self, lines):
        super().__init__(lines)
        self.lines = lines # store for future reset

    def test_and_run(self):
        r = range(0,len(self.memory))
        for flip_pointer in r:
            operation, argument = self.memory[flip_pointer]
            if operation == 'jmp':
                self.memory[flip_pointer] = ('nop', argument)
            elif operation == 'nop':
                self.memory[flip_pointer] = ('jmp', argument)
            if self.run_until_loop():
                return self.accumulator
            else:
                self.reset(self.lines)
        return self.accumulator

if __name__ == '__main__':
    cpu = CPU2(read_input())
    cpu.test_and_run()
    print(cpu.accumulator)
