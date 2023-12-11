with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

maps = {'L': ['$|$', '$o-', '$$$'],
        'J': ['$|$', '-o$', '$$$'],
        'F': ['$$$', '$o-', '$|$'],
        '7': ['$$$', '-o$', '$|$'],
        '-': ['$$$', '-o-', '$$$'],
        '|': ['$|$', '$o$', '$|$'],
        '.': ['$$$', '$o$', '$$$'],
        'S': ['$s$', 'sSs', '$s$']}
class Vertex:
    def __init__(self, position, previous, steps):
        self.position, self.previous, self.steps = position, previous, steps
        self.next = None

grid = [''.join([maps[d][i] for d in line]) for line in input for i in range(0,3)]
start = Vertex([(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 'S'][0], None, 0)
current = [(start.position[0] - 2*i,start.position[1]) for i in [-1, 1] if grid[start.position[0] - 2*i][start.position[1]] in '|-']
# ---------------------------------------- Del 1 -------------------------------------------

# ---------------------------------------- Del 2 -------------------------------------------