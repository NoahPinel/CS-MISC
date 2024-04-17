def O():
    return 0

def succ(n):
    return n + 1

def to_peano(n):
    if n == 0:
        return O()
    else:
        return succ(to_peano(n - 1))

def add(m, n):
    if m == O():
        return n
    else:
        return add(m - 1, succ(n))

def peano_to_string(peano_ENC):
    if peano_ENC == O():
        return '0'
    return 'S(' + peano_to_string(peano_ENC - 1) + ')'

def peano_decode(peano_ENC, count):
    pass
    #TODO
    # Add unwrapping for peano_ENC
    # That is, show the full derivation 

x = 1
y = 3

print(peano_to_string(x))
print(peano_to_string(y))

# cast add() result into Succ form (S (S .... (0) .... ) )
result_add = add(x, y)
print(result_add)
encoded = peano_to_string(result_add)
print(encoded)
peano_decode(encoded, 0)
