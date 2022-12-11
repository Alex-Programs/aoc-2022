with open("input.txt") as f:
    data = f.read().split("\n")

import math
class CPU():
    def __init__(self, cycle=1, x_register=1):
        self.cycle = cycle
        self.x_register = x_register
        self.cycle_register_history = {}
        self.cycle_signal_history = {}

    def run_cycle(self, instruction, opcodes):
        match instruction:
            case "noop":
                self.cycle_register_history[self.cycle] = self.x_register
                self.cycle_signal_history[self.cycle] = self.x_register * self.cycle
                self.cycle += 1

            case "addx":
                for i in range(2):
                    self.cycle_register_history[self.cycle] = self.x_register
                    self.cycle_signal_history[self.cycle] = self.x_register * self.cycle
                    self.cycle += 1

                self.x_register += int(opcodes[0])

cpu = CPU()

for line in data:
    instruction, *opcodes = line.split(" ")
    cpu.run_cycle(instruction, opcodes)

p1 = 0
for i in range(20, 1000, 40):
    if not cpu.cycle_register_history.get(i):
        break

    score = cpu.cycle_register_history[i] * i
    print(f"Cycle {i} - X register: {cpu.cycle_register_history[i]} - Score: {score}")
    p1 += score

print(f"Part 1: {p1}")

pixels = []

# Part 2

display = ""

for i in range(1, cpu.cycle):
    offset = (math.floor(i/40)*40)+1

    valid_locations = [i-offset-1, i-offset,i-offset+1]
    if cpu.cycle_register_history.get(i) in valid_locations:
        display += "█"
    else:
        display += " "

    if i % 40 == 0:
        display += "\n"

print("Part 2:")
print(display)