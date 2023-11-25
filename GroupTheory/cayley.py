import sys
width = 3

if len(sys.argv) > 1:
    mod = int(sys.argv[1])
else:
    print("Please provide n such that z/z_n can be built.")
    sys.exit(1)

if len(sys.argv) > 2:
    operation = sys.argv[2]
    if operation not in ['+', '*']:
        print("Invalid group operation, either + or * ")
        sys.exit(1)
else:
    operation = '+'

print('  ' * width, end='')
for i in range(mod):
    print(f'{i:>{width}} |', end='')

for i in range(mod):
    print(f'\n{i:>{width}} |', end=' ')
    for j in range(mod):
        if operation == '+':
            out = (i + j) % mod
        else:
            out = (i * j) % mod
        print(f'{out:>{width}} ', end=' ')
print('\n')

