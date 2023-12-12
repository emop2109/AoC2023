with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

class Spring:
    def __init__(self, type):
        self.type = type
        self.next = []
# ---------------------------------------- Del 1 -------------------------------------------
def build_tree(spring, line):
    if len(line):
        if line[0] == '?':
            _spring_alt_1, _spring_alt_2 = Spring('.'), Spring('#')
            spring.next.extend([_spring_alt_1, _spring_alt_2])
            build_tree(_spring_alt_1, line[1:])
            build_tree(_spring_alt_2, line[1:])
        else:
            _spring_ = Spring(line[0])
            spring.next.append(_spring_)
            build_tree(_spring_, line[1:])
def get_string(spring, msg):
starts = []
for line in input:
    spring = Spring(None)
    starts.append(spring)
    build_tree(spring, line.split(' ')[0])

# ---------------------------------------- Del 2 -------------------------------------------

