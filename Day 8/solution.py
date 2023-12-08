import re
import math

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

instructions = input[0]
nodes = {x : (y,z) for (x,y,z) in [re.findall(r'\w+', input[n]) for n in range(2,len(input))]}

def get_number_of_steps(s, function):
    current_position, steps = s, 0
    while function(current_position):
        for i in instructions:
            current_position = nodes[current_position][0] if i == 'L' else nodes[current_position][1]
            steps += 1
            if not function(current_position):
                return steps
    return steps
# ---------------------------------------- Del 1 -------------------------------------------
def func_1(s):
    return s != 'ZZZ'
print(get_number_of_steps('AAA', func_1))
# ---------------------------------------- Del 2 -------------------------------------------
current_positions, steps = [x for x in nodes if x[-1] == 'A'], []
def func_2(s):
    return 'Z' not in s

for c in current_positions:
    steps.append(get_number_of_steps(c, func_2))

print(math.lcm(*steps))