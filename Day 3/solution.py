import re
import math

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()
symbols = {(row,column) : [] for row in range(len(input)) for column in range(len(input[0])) if input[row][column] not in '.0123456789'}
# ---------------------------------------- Del 1 -------------------------------------------
for row, line in enumerate(input):
    for m in re.finditer(r'\d+', line):
        adjacent = [(r, column) for r in (row - 1, row, row + 1) for column in range(m.start() - 1, m.end() + 1)]
        for adj in adjacent:
            if adj in symbols.keys():
                symbols[adj].append(int(m.group()))
_sum_ = 0
for key in symbols:
    _sum_ += sum(symbols[key])
print(_sum_)
# ---------------------------------------- Del 2 -------------------------------------------
print(sum([math.prod(p) for p in symbols.values() if len(p) == 2]))
