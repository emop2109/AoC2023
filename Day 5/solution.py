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
        self.maps, self.ranges, self._min_ = maps, ranges, 100_000_000_00

    def addranges(self, range):
        x_0, x_1 = range
        for (dest, source, r) in self.maps:
            if x_0 == x_1:
                break
            if x_1 <= source:
                self.ranges.append(tuple([x_0, x_1]))
                break
            elif x_0 < source:
                self.ranges.append(tuple([x_0, source]))
                x_0 = source
            elif source <= x_0 < source + r:
                self.ranges.append(tuple([dest + x_0 - source, dest + min(x_1, source + r) - source]))
                x_0 = min(x_1, source + r)
        """ if x_0 != x_1:
            self.ranges.append(tuple([x_0, x_1])) """
        self._min_ = min(self.ranges)[0]

def apply_ranges(seeds):
    layers = [Layer(maps=maps[keys], ranges=[]) for keys in maps]
    layers.insert(0,Layer(ranges=seeds))
    for n in range(1,len(layers)):
        for sets in layers[n-1].ranges:
            layers[n].addranges(sets)
    return layers[-1]._min_
# ---------------------------------------- Del 1 -------------------------------------------
print(apply_ranges([tuple([seeds[i], seeds[i]+1]) for i in range(0, len(seeds))]))

# ---------------------------------------- Del 2 -------------------------------------------
print(apply_ranges([tuple([seeds[i], seeds[i]+seeds[i+1]]) for i in range(0, len(seeds), 2)]))