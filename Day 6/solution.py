import re
import math

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

races = [tuple([int(t),int(d)]) for t,d in zip(re.findall(r'\d+', input[0]), re.findall(r'\d+', input[1]))]
# ---------------------------------------- Del 1 -------------------------------------------
wins = 1
for (time,distance) in races:
    _win_ = 0
    for i in range(1, time - 1):
        _win_ += 1 if i*(time - i) > distance else 0
    wins *= _win_ if _win_ != 0 else 1
print(wins)
# ---------------------------------------- Del 2 -------------------------------------------
race = tuple([int(''.join([x for x in re.findall(r'\d+', input[0])])), int(''.join([x for x in re.findall(r'\d+', input[1])]))])
t1, t2 = (-race[0] + math.sqrt(race[0]**2-4*race[1]))/2, (-race[0] - math.sqrt(race[0]**2-4*race[1]))/2
print(round(t1-t2))