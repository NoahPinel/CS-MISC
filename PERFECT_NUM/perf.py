primes = [2, 3, 5, 7, 11, 13]

def factor(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    print('+'.join(map(str, divs)), end=' =')
    print(' {}'.format(sum(divs)))

def per(primes):
    for i in primes:
        perfect = (pow(2, i) - 1) * pow(2, i - 1)
        print(perfect)
        factor(perfect)
        print('\n')

per(primes)

