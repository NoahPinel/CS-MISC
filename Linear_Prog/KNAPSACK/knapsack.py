from pulp import *
import random

def random_list(n):
    my_list = []
    for _ in range(n):
        my_list.append(random.randint(1, 20))
    return my_list

def random_carry():
    return random.randint(5, 30)

def random_size():
    return random.randint(1, 11)

n = random_size()
weights = random_list(n)
prices = random_list(n)

print(f'n = {n}')
print('Random W and P')
print(weights)
print(prices)
max_carry = random_carry()

model = LpProblem(sense=LpMaximize)
variables = [LpVariable(name=f"item_index_{i}", cat=LpBinary) for i in range(n)]
model += lpDot(weights, variables) <= max_carry
model += lpDot(prices, variables)

status = model.solve(PULP_CBC_CMD(msg=False))
print('price: ', model.objective.value())

print('What to pack!')
for i, variable in enumerate(variables):
    if (variable.value() == 1):
        print(f'{variable.name}: x1')
