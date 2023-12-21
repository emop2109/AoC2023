import re

with open('.\input.txt', 'r') as file:
    input=file.read()
(workflow, *raitings) = input.split('\n\n')

class HeapNode:
    def __init__(self, next, value = -1, comparison='#'):
        self.value, self.next, self.comparison = value, next, comparison
    
    def get_next_value(self, x = -10):
        if self.value == -1:
            return self.next
        if self.comparison == '>':
            return self.next if x > self.value else False
        return self.next if x < self.value else False
    
workflows = {}
for line in workflow.splitlines():
    workflows[line.split('{')[0]] = [x for x in line.split('{')[1].replace('}', '').split(',')]

print(workflows)
# ---------------------------------------- Del 1 -------------------------------------------

# ---------------------------------------- Del 2 -------------------------------------------

