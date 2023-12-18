with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()
instructions = [line.split(' ')[:2] for line in input]
directions = {'U': (-1,0), 'R': (0,1), 'D': (1,0), 'L': (0,-1)}

def calculate_area():
    x0, y0, area, boundary = 0, 0, 0, 0
    for line in instructions:
        x1, y1 = x0 + int(line[1])*directions[line[0]][0], y0 + int(line[1])*directions[line[0]][1]
        area += (x0*y1-y0*x1)
        boundary += (abs(x1-x0) + abs(y1-y0))
        x0, y0 = x1, y1
    return abs(area)//2 + boundary//2 + 1
# ---------------------------------------- Del 1 -------------------------------------------
print(calculate_area())
# ---------------------------------------- Del 2 -------------------------------------------
directions = {3: (-1,0), 0: (0,1), 1: (1,0), 2: (0,-1)}
instructions = [(int(line.split(' ')[-1][-2]), int(line.split(' ')[-1][2:-2], 16)) for line in input]
print(calculate_area())


