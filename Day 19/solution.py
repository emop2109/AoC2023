import re, math
with open('.\input.txt', 'r') as file:
    input=file.read()
(workflow, *raitings), workflows = input.split('\n\n'), {}
for flow in workflow.split('\n'):
    workflows[flow.split('{')[0]] = [x.replace('}', '') for x in flow.split('{')[1].split(',')]
# ---------------------------------------- Del 1 -------------------------------------------
current_workflow, _sum_, dict_values = 'in', 0, {'x': 0, 'm': 1, 'a': 2, 's': 3}

def get_next_workflow(current_workflow, values):
    for alternatives in workflows[current_workflow]:
        if ':' not in alternatives:
            return alternatives
        if eval(f'{values[dict_values[alternatives[0]]]}{alternatives.split(":")[0][1:]}'):
            return alternatives.split(':')[1]

_sum_ = 0
for line in raitings[0].split('\n'):
    current_workflow, values = 'in', list(map(int, re.findall(r'\d+', line)))
    while current_workflow not in 'RA':
        current_workflow = get_next_workflow(current_workflow, values)
    _sum_ += sum(values) if current_workflow == 'A' else 0
print(_sum_)
# ---------------------------------------- Del 2 -------------------------------------------
class Node:
    def __init__(self, name, values=[(1,4000)]*4):
        self.name, self.values, self.nodes = name, values, []

def get_possibilities(range, string):
    a_l, a_u = range
    limit = int(re.findall(r'\d+', string)[0])
    if '<' in string:
        inside = (a_l, min(limit - 1, a_u)) if a_l < limit else (0,0)
        outside = (max(a_l, limit), a_u) if a_u > limit else (0,0)
    else:
        inside = (max(a_l, limit + 1), a_u) if a_u > limit else (0,0)
        outside = (a_l, min(limit, a_u)) if a_l < limit else (0,0)
    return outside, inside

def depth_first_search(start):
    queue, _sum_ = [start], 0
    while queue:
        node = queue.pop(0)
        if node.name == 'A':
            _sum_ += math.prod([x[1] - x[0] + 1 for x in node.values])
        elif node.name != 'R':
            _in, _out = [values for values in node.values], [values for values in node.values]
            for alternatives in workflows[node.name]:
                if ':' in alternatives:
                    _out[dict_values[alternatives[0]]], _in[dict_values[alternatives[0]]] = get_possibilities(_in[dict_values[alternatives[0]]], alternatives)
                    node.nodes.append(Node(alternatives.split(':')[1], [v for v in _in]))
                    _in[dict_values[alternatives[0]]] = _out[dict_values[alternatives[0]]]
                    queue.append(node.nodes[-1])
                else:
                    node.nodes.append(Node(alternatives, _out))
                    queue.append(node.nodes[-1])
    print(_sum_)
depth_first_search(Node('in'))