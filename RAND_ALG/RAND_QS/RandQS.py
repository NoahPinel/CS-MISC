"""
RandQS: Randomized QuickSort
using algo from the text "Randomized Algorithms"
by Prabhakar Raghavan and Rajeev Motwani

Input:
A set of numbers S.

Output:
The elements of set S, sorted in increasing order.

Steps:
1. Choose an element y uniformly at random from set S: every element in S 
has an equal probability of being chosen as the pivot (i.e. 1/n).

2. By comparing each element of S with the pivot element (y), determine 
the set S1 of elements smaller than y and the set S2 of elements larger than y.

3. Recursively sort S1 and S2 using the same Randomized QuickSort algorithm.
    3.1. note that I have included this, but am using native .sort()

4. Output the sorted version of S1, followed by the pivot element (y), and then the sorted version of S2.

Note:
The Pseudocode from the text calls for recursive descent, I included it, but sort() will be faster hence why
I have used it.


Some math:
for the native algo, using recursion we have the following for E[# of comparisons]
This is clearly:
    \sum_{i=1}^{n}\sum_{j>i}E[X_{ij}]

Using this we can got to show that there is indeed an upper bound for # of comparisons, 
which is:
    2nH_n
    where H_n := \sum_{k=1}^{n} 1/k

Thus giving us the theorem: The expected number of comparisons in an execution of RandQS is at most 2nH_n.

And finally, we conclude that the expected running time is O(n log n)
"""
import random

def rand_qs(S):
    if len(S) <= 1:
        return S

    index = random.randint(0, len(S) - 1)
    y = S[index]

    S1, S2 = [], []
    for element in S:
        if element < y:
            S1.append(element)
        elif element > y:
            S2.append(element)

    # Recursively sort S1 and S2
    #sorted_S1 = rand_qs(S1)
    #sorted_S2 = rand_qs(S2)
    
    S1.sort()
    S2.sort()
    
    fin_sort = S1 + [y] + S2
    return fin_sort

S = []
with open("input.txt", "r") as file:
    S = [int(num) for num in file.read().strip().split(',')]

print(S)
sorted_S = rand_qs(S)
print(sorted_S)
