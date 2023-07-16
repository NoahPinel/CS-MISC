"""
Turing Machine Palindrome Checker (PAL)

This Python program emulates a Turing machine to determine whether a given bit string is a palindrome. 
It takes a binary string as input and processes it through the Turing machine to determine whether it 
reads the same forwards and backwards.


Input:
    - <bit_string>: A binary string to be checked for palindromic property.

Output:
    - If the input bit string is a palindrome, the output tape will read 1
    - If the input bit string is not a palindrome, the output tape will read 0

Algorithm:
    1. Initialize the Turing machine with the input bit string.
    2. Traverse the tape from left to right while comparing each symbol with its counterpart on the opposite side.
    3. If a mismatch is found, the input is not a palindrome.
    4. If the tape is fully traversed without finding a mismatch, the input is a palindrome.

Example Usage:
    $ python pal.py 1001
    HALTED
	OUTPUT TAPE: 1


    $ python pal.py 11010
    HALTED
	OUTPUT TAPE: 0
"""
def get_string():
    string = []
    tmp = input('Enter {0, 1}^*: ')
    for char in tmp:
        string.append(char)
    return string

def copy_in_tape(inp_tape):
    return inp_tape[::-1]

"""
This is how PAL is described classicaly,
start one head at the START of input tape,
then the other head at the END of the copied tape,
im just using input for simplicity, but it will work 
the same. Set pointers so they compare front to back 
and if any != HALT.
"""
def Classic_PAL(input):
    # Set bound, tape will be ==
    Up_bound = len(input)
    # set input tape index
    i = 0
    j = len(input) -1 
    while i < Up_bound and j >= 0:
        # compare
        if (input[i] != input[j]):
            print('HALTED')
            print('OUTPUT TAPE: 0')
            return 0
        i += 1
        j -= 1
    print('HALTED')
    print('OUTPUT TAPE: 1')

"""
 This is another way to do the simulation,
 pass in a input tape and a copy of it, note
 though that the copy has been reversed.
"""
def PAL(input, copied):
    # Set bound, tape will be ==
    Up_bound = len(input)
    # set input tape index
    i = 0
    while i < Up_bound:
        # compare
        if (input[i] != copied[i]):
            print('HALTED')
            print('OUTPUT TAPE: 0')
            return 0
        i += 1
    print('HALTED')
    print('OUTPUT TAPE: 1')

def main():
    inp_tape = get_string()
    print(inp_tape)

    copy_tape = copy_in_tape(inp_tape)
    print(copy_tape)

    Classic_PAL(inp_tape)
    PAL(inp_tape, copy_tape)
main()
