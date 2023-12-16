with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

def depth_first_search(start_position):
    visited, queue = [], [start_position]
    while len(queue):
        position, directions = queue.pop()
        if (position,directions) not in visited:
            if -1 < position[0] < len(input) and -1 < position[1] < len(input[0]):
                if input[position[0]][position[1]] == '\\':
                    queue.append(((position[0] + directions[1], position[1] + directions[0]), (directions[1], directions[0])))
                elif input[position[0]][position[1]] == '/':
                    queue.append(((position[0] - directions[1], position[1] - directions[0]), (-directions[1], -directions[0])))
                elif input[position[0]][position[1]] == '|' and directions[1] != 0:
                    queue.append(((position[0] - directions[1], position[1] - directions[0]), (-directions[1], -directions[0])))
                    queue.append(((position[0] + directions[1], position[1] + directions[0]), (directions[1], directions[0])))
                elif input[position[0]][position[1]] == '-' and directions[0] != 0:
                    queue.append(((position[0] - directions[1], position[1] - directions[0]), (-directions[1], -directions[0])))
                    queue.append(((position[0] + directions[1], position[1] + directions[0]), (directions[1], directions[0])))
                else:
                    queue.append(((position[0] + directions[0], position[1] + directions[1]),directions))
                visited.append((position, directions))
    return visited
# ---------------------------------------- Del 1 -------------------------------------------
visited = set([x[0] for x in depth_first_search(((0,0), (0,1)))])
print(len(visited))
# ---------------------------------------- Del 2 -------------------------------------------
vertical = max([len(set([x[0] for x in depth_first_search(((len(input)*n, c),((-1)**n,0)))])) for n in [0, 1] for c in range(len(input[0]))])
horizontal = max([len(set([x[0] for x in depth_first_search(((r, len(input[0])*n),(0,(-1)**n)))])) for n in [0, 1] for r in range(len(input))])
print(max(vertical, horizontal))