import re
with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

class Bricks:
    def __init__(self, cubes):
        self.cubes, self.over, self.under = cubes, set(), set()
bricks = [Bricks(list(map(int, re.findall(r'\d+', line)))) for line in input]
bricks.sort(key=lambda x: x.cubes[2])

def ontop_of(a, b):
    return min(a.cubes[3], b.cubes[3]) >= max(a.cubes[0], b.cubes[0]) and min(a.cubes[4],  b.cubes[4]) >= max(a.cubes[1], b.cubes[1])

for i in range(len(bricks)):
    max_z = 1
    for j in range(i - 1, -1, -1):
        if ontop_of(bricks[i], bricks[j]):
            max_z = max(bricks[j].cubes[-1] + 1, max_z)
    bricks[i].cubes[5] -= bricks[i].cubes[2] - max_z
    bricks[i].cubes[2] = max_z
bricks.sort(key=lambda x: x.cubes[2])
for i in range(len(bricks) - 1):
    for j in range(i + 1, len(bricks)):
        if ontop_of(bricks[i], bricks[j]) and bricks[i].cubes[-1] + 1 == bricks[j].cubes[2]:
            bricks[i].over.add(bricks[j])
            bricks[j].under.add(bricks[i])
# ---------------------------------------- Del 1 -------------------------------------------
total = 0
for brick in bricks:
    if len(brick.over) == 0:
        total += 1
    else:
        if all([len(b.under) > 1 for b in brick.over]):
            total += 1
print(total)
# ---------------------------------------- Del 2 -------------------------------------------
total = 0
for brick in bricks:
    falling, queue = set({brick}), [brick]
    while len(queue):
        current_brick = queue.pop(0)
        for b in current_brick.over:
            if len(b.under) == len(falling.intersection(set(b.under))):
                queue.append(b)
                falling.add(b)
    total += len(falling) - 1
print(total)

