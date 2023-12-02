import re

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

_max_ = {'red': 12, 'green': 13 ,'blue': 14}

# ---------------------------------------- Del 1 -------------------------------------------

def check_moves(moves):
    for (number, key) in moves:
        if int(number) > _max_[key]:
            return False
    return True

id_sum = 0
for idx, game in enumerate(input):
    moves = re.findall(r'(\d+)\s+(red|green|blue)', game)
    id_sum += (idx+1) if check_moves(moves) else 0

print(id_sum)

# ---------------------------------------- Del 2 -------------------------------------------
sum = 0
for idx, game in enumerate(input):
    _dict_ = {'red': 0, 'green': 0, 'blue': 0}
    moves = re.findall(r'(\d+)\s+(red|green|blue)', game)
    for (number, key) in moves:
        _dict_[key] = max(int(number), _dict_[key])
    sum += (_dict_['red']*_dict_['green']*_dict_['blue'])

print(sum)