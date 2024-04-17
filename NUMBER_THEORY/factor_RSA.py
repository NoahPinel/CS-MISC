# In RSA it is key =) not to let Eve find \phi(N), for if she knew it, she could find
# the value's p and q from the public N. Note, with knowledge of \phi(N), factoring
# N can be done in time O(1).
#
#
# Recall: N = pq, p and q are prime and p is not the same as q.
# 
# If we get a hold of \phi(N), recovery of p and q is done as follows:
#
# i) N = pq, \phi(N) = (p-1)(q-1) = pq - p - q + 1 = (N+1) - (p+q)
#
# ii) We can then derive the quadratic in p: N = p^2 + p(N+1-\phi(N)) + N = 0
#
# iii) From here we just solve the equation, the roots will be p and q.
import sys
import math


def Factor_N(N, phi):
    b = N + 1 - phi
    disc = pow(abs(b), 2) - (4 * N)
    p = (b + math.sqrt(disc)) // 2
    q = (b - math.sqrt(disc)) // 2

    print(p)
    print(q)


def main():
    if len(sys.argv) != 3:
        print("ERROR")
        print("Usage: python3 factor_RSA.py <N> <phi(N)>")
        return

    N = int(sys.argv[1])
    phi = int(sys.argv[2])
    Factor_N(N, phi)


main()
