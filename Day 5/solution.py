import re

with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()
seeds, maps = [int(x) for x in re.findall(r'\d+', input[0])], {x: [] for x in input[1:] if ':' in x}
for keys in maps:
    i = input.index(keys) + 1
    while i < len(input) and input[i] != '':
        maps[keys].append(tuple([int(x) for x in re.findall(r'\d+', input[i])]))
        i += 1
    maps[keys] = sorted(maps[keys], key=lambda x:x[1])

class Layer:
    def __init__(self, maps=None, ranges = []):
        self.maps = maps
        self.ranges = ranges
    
    def addranges(self, range):
        x_0, x_1 = range
        for (dest, source, r) in self.maps:
            if x_1 <= source:
                self.ranges.append(tuple([x_0, x_1]))
                x_0 = x_1
                break
            elif x_0 < source:
                self.ranges.append(tuple([x_0, source]))
                x_0 = source
            elif x_0 > source + r:
                self.ranges.append(tuple([x_0, x_1]))
                x_0 = x_1
            elif x_0 >= source:
                self.ranges.append(tuple([dest + x_0 - source, dest + min(x_1, source+ r) - source]))
                x_0 = min(x_1, source+r)
        if x_0 != x_1:
            self.ranges.append(tuple([x_0, x_1]))

layers = [Layer(maps=maps[keys], ranges=[]) for keys in maps]
layers.insert(0,Layer(ranges=[tuple([seeds[i], seeds[i]+seeds[i+1]]) for i in range(0, len(seeds), 2)]))
# ---------------------------------------- Del 1 -------------------------------------------
for n in range(1,len(layers)):
    for sets in layers[n-1].ranges:
        layers[n].addranges(sets)
_min_ = 100_000
for layer in layers:
    print(layer.ranges)
for sets in layers[-1].ranges:
    _min_ = min(_min_, sets[0])
print(_min_)

""" for i in range(len(seeds)):
    for keys in maps:
        for (dest, source, r) in maps[keys]:
            if seeds[i] in range(source, source+r):
                seeds[i] = int((dest+seeds[i]-source))
                break
print(min(seeds)) """
# ---------------------------------------- Del 2 -------------------------------------------
seeds = [int(x) for x in re.findall(r'\d+', input[0])]
seeds_set = {x : [[x]] for x in[tuple([seeds[i], seeds[i]+seeds[i+1]]) for i in range(0, len(seeds), 2)]}
""" for seed in seeds_set:
    for keys in maps:
        sets = seeds_set[seed][-1]
        for (s, e) in sets:
            for (dest, source, r) in maps[keys]:
                if s < source: """



