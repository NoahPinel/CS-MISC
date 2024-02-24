# The Pr(X) that any two integral values
# are co-prime has been proved to be 
# 6/pi^2 ~= 0.6079
# 
# This code is simply just simulating this!
import random
import math

def sim(sample):
    coprime_count = 0
    for i in range(sample):
        x = random.randint(1, 1_000_000_000)
        y = random.randint(1, 1_000_000_000)
        gcd = math.gcd(x,y)
        if (gcd == 1):
            coprime_count += 1

    ratio = coprime_count / sample 
    print(f'Total : {sample}')
    print(f'Co-prime : {coprime_count}')
    print(ratio)

sim(100000)
