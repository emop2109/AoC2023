with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

maps = {'L': ['#|#', '#o-', '###'],
        'J': ['#|#', '-o#', '###'],
        'F': ['###', '#o-', '#|#'],
        '7': ['###', '-o#', '#|#'],
        '-': ['###', '-o-', '###'],
        '|': ['#|#', '#o#', '#|#'],
        '.': ['###', '#o#', '###'],
        'S': ['#s#', 'sSs', '#s#']}
class Vertex:
    def __init__(self, position, previous, steps):
        self.position, self.previous, self.steps = position, previous, steps
        self.next = None

grid = [''.join([maps[d][i] for d in line]) for line in input for i in range(0,3)]
with open('output.txt', 'w') as file:
    for line in grid:
        file.writelines(line+'\n')
def get_vertices():
    start = Vertex([(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 'S'][0], None, 0)
    vertices = [(start.position[0] - 2*i*(1-n),start.position[1] - 2*i*n) for i in [-1, 1] for n in [0, 1]if grid[start.position[0] - 2*i*(1-n)][start.position[1] - 2*i*n] in '|-'][0]
    start.next = Vertex(((vertices[0]-start.position[0])/2+start.position[0], (vertices[1]-start.position[1])/2+start.position[1]), start, start.steps+1)
    current = Vertex((vertices[0], vertices[1]), start.next, start.next.steps+1)
    start.next.next = current
    return start, current

def adjacent_vertices(vertex):
    for pos in [(vertex.position[0] - i*(1-n),vertex.position[1] - i*n) for i in [-1, 1] for n in [0, 1] if grid[vertex.position[0] - i*(1-n)][vertex.position[1] - i*n] in 'o|-sS']:
        if pos != vertex.previous.position:
            return pos

# ---------------------------------------- Del 1 -------------------------------------------
start, current = get_vertices()
vertices = [start.position, start.next.position, current.position]
while current.position != start.position:
    current.next = Vertex(adjacent_vertices(current), current, current.steps+1)
    current = current.next
    vertices.append(current.position)
current.next = start
print((current.previous.steps+1)//6)
# ---------------------------------------- Del 2 -------------------------------------------
def adjacent_directions(position, queue):
    return [(position[0] + i, position[1] + n) for i in [-1,0,1] for n in [-1,0,1] if (position[0] + i, position[1] + n) not in queue]
visited, queue = [], [(219,219)]
while len(queue):
    position = queue.pop()
    if position not in visited and position not in vertices:
        queue.extend(adjacent_directions(position, queue))
        string_list = list(grid[position[0]])
        string_list[position[1]] = 'I' if grid[position[0]][position[1]] == 'o' else '#'
        grid[position[0]] = ''.join(string_list)
        visited.append(position)
print(sum([1 for r in range(len(grid)) for c in range(grid[0]) if grid[r][c] == 'I']))