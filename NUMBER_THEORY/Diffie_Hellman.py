# A very simple Diffe-Hellman implementation

import random
from sympy import factorint 

def prim_root(N):
    # p prime so we can do the following
    phi = N - 1
    factor = factorint(phi)
    
    '''
    Algo works by getting all factors of phi(N), then we simply apply
    the primitive root test, checking that all factors are not of the
    form g^{N-1/2} \equiv 1 (mod N).
    If current g fails this test, break, loop again
    If current g passes for ALL factors, return, as we are taking the smallest
    g for simplicity.
    '''
    for g in range(2, N):
        is_prim_root = True
        for p, exp in factor.items():
            if pow(g, (N-1)//p, N) == 1:
                is_prim_root = False
                break
        if is_prim_root:
            return g


def Calc_Shared(g, N):
    sec_val = random.randint(2, N-2)
    Shared = pow(g, sec_val, N)
    return sec_val, Shared


def Key_Gen(Pub, priv, N):
    K = pow(Pub, priv, N)
    return K


def main():
    N = 7919
    g = prim_root(N)
    a, A = Calc_Shared(g, N)
    b, B = Calc_Shared(g, N)
    ka = Key_Gen(B, a, N)
    kb = Key_Gen(A, b, N)
    
    # Simulate the algo.
    print('Eve can see:')
    print('N = {}'.format(N))
    print('g = {}'.format(g))
    print('A = {}'.format(A))
    print('B = {}'.format(B))
    print('Eve can NOT see:')
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('\nAlice chooses the secret value {}'.format(a))
    print('Alice computes A = {}'.format(A))
    print('\nBob chooses the secret value {}'.format(b))
    print('Bob computes B = {}'.format(B))
    print('\nAlice Sends A to Bob')
    print('Bob Sends B to Alice')
    print('\nAlice receives B')
    print('Alice computes K = {}'.format(ka)) 
    print('\nBob receives A')
    print('Bob computes K = {}'.format(kb)) 
    print('\nAs we can see K_a = {} = {} = K_b'.format(ka, kb))
main()
