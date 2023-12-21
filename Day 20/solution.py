import math
with open('.\input.txt', 'r') as file:
    input=file.read().splitlines()

class BaseModule:
    def __init__(self, name):
        self.name, self.lows, self.highs = name, 0, 0
        self.modules = []
        self.cycle = []
    
    def add_module(self, module):
        self.modules.append(module)

class BroadcasterModule(BaseModule):
    def __init__(self, name):
        super().__init__(name)
    
    def send_signal(self):
        for module in self.modules:
            module.recieve_signal(0, self.name)
        self.lows += len(self.modules)
        return self.modules

class FlipflopModule(BaseModule):
    def __init__(self, name):
        super().__init__(name)
        self.state, self.current_signal = 'Off', 0
        self.send_si = False

    def recieve_signal(self, signal, name):
        if signal == 0:
            self.state = 'On' if self.state == 'Off' else 'Off'
            self.send_si = True
    
    def send_signal(self):
        recieve_modules = []
        if self.send_si:
            for module in self.modules:
                module.recieve_signal(0 if self.state == 'Off' else 1, self.name)
                recieve_modules.append(module)
            self.lows += len(recieve_modules) if self.state == 'Off' else 0
            self.highs += 0 if self.state == 'Off' else len(recieve_modules)
        self.send_si = False
        return recieve_modules
    
class ConjuctionModule(BaseModule):
    def __init__(self, name, inputs):
        super().__init__(name)
        self.states = {x.replace(' ','') : 0 for x in inputs}

    def recieve_signal(self, signal, name):
        self.states[name] = signal

    def send_signal(self):
        signal = 0 if all([x == 1 for x in self.states.values()]) else 1
        for module in self.modules:
            module.recieve_signal(signal, self.name)
        self.lows += len(self.modules) if signal == 0 else 0
        self.highs += len(self.modules) if signal == 1 else 0
        return self.modules

class OutputModule(BaseModule):
    def __init__(self, name):
        super().__init__(name)
        self.recieved_signal = 1
    def recieve_signal(self, signal, name):
        self.recieved_signal = signal
    def send_signal(self):
        return []

def get_module(name, modules):
    for module in modules:
        if module.name == name:
            return module
modules = []
for line in input:
    if '%' in line:
        modules.append(FlipflopModule(line.split(' -> ')[0][1:]))
    elif '&' in line:
        inputs = [x.split('->')[0].replace('%','').replace('&','') for x in input if line.split(' -> ')[0][1:] in x.split('->')[1]]
        modules.append(ConjuctionModule(line.split(' -> ')[0][1:], inputs))
    else:
        modules.append(BroadcasterModule('broadcaster'))

for line in input:
    module = get_module(line.split(' -> ')[0].replace('%', '').replace('&', ''), modules)
    for mod in line.split(' -> ')[1].split(','):
        m = get_module(mod.replace(' ', ''), modules)
        if m is not None:
            module.add_module(m)
        else:
            output = OutputModule(mod.replace(' ', ''))
            module.add_module(output)
            modules.append(output)
            
# ---------------------------------------- Del 1 -------------------------------------------
def simulate_signals(broadcaster, i):
    queue = [broadcaster]
    while queue:
        module = queue.pop(0)
        try:
            if any([x == 0 for x in module.states.values()]):
                module.cycle.append(i)
        except:
            pass
        queue.extend(module.send_signal())
broadcaster = get_module('broadcaster', modules)
for i in range(10000):
    simulate_signals(broadcaster, i)
print((1000+sum([m.lows for m in modules]))*sum([m.highs for m in modules]))
# ---------------------------------------- Del 2 -------------------------------------------
def get_next_to_output_module(output, modules):
    for module in modules:
        for mod in module.modules:
            if mod.name == output:
                return module
x = [get_module(x, modules) for x in get_next_to_output_module('rx', modules).states]
cycles = [module.cycle[1] - module.cycle[0] for module in x]
print(math.lcm(*cycles))