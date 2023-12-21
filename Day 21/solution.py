import numpy as np

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

grid = [[c for c in r] for r in input]

def get_start():
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                return (r,c)
start = get_start()
# ---------------------------------------- Del 1 -------------------------------------------
def calculate_steps(position):
    _ = []
    for _x,_y in ((-1,0), (1, 0), (0, -1), (0, 1)):
        x, y = position[0] + _x , position[1] + _y
        if -1 < x < len(grid) and -1 < y < len(grid[x]) and grid[x][y] != '#':
            _.append((x,y))
    return _
def simulate_steps(start, n, function):
    queue = set([start])
    for _ in range(n):
        temp = [x for x in queue]
        queue = set()
        for step in temp:
            queue.update(function(step))
    return queue

print(len(simulate_steps(start, 64, calculate_steps)))
# ---------------------------------------- Del 2 -------------------------------------------
grid[start[0]][start[1]] = '.'

def calculate_infinite_steps(position):
    _ = []
    for _x, _y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = position[0] + _x, position[1] + _y
        x_, y_ = x, y
        if x < 0 or x > len(grid) - 1:
            x_ = abs(x)%(len(grid)) if x > len(grid) - 1 else len(grid) - 1 - (abs(x)-1)%(len(grid))
        if y < 0 or y > len(grid[0]) - 1:
            y_ = abs(y)%(len(grid[0])) if y > len(grid[0]) - 1 else len(grid[0]) - 1 - (abs(y)-1)%(len(grid[0]))
        if grid[x_][y_] != '#':
            _.append((x, y))
    return _

def calculate_polynomial(values):
    coefficients = np.polyfit(*zip(*values), 2)
    print(round(np.polyval(coefficients, 202300)))
calculate_polynomial([(i, len(simulate_steps(start, 65 + i*131, calculate_infinite_steps))) for i in range(3)])