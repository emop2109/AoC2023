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
def simulate_steps(start, n):
    queue = set([start])
    for _ in range(n):
        temp = [x for x in queue]
        queue = set()
        for step in temp:
            queue.update(calculate_steps(step))
    return queue

print(len(simulate_steps(start, 64)))
# ---------------------------------------- Del 2 -------------------------------------------

