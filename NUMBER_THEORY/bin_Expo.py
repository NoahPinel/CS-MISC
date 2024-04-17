# Binary exponentiation algorithm to compute Alice’s public key
#
# Need (e,N) and g or M (Works the same)
def Bin_Expo(M, e, N):
    result = 1
    carry = M
    e_bin = bin(e)[2:]
    for bit in e_bin:
        result = (result * result) % N
        if bit == '1':
            result = (result * carry) % N
    
    return result

def main():
    # Plaintext
    M = 2
    # Pub key
    e = 9
    N = 11
    print(Bin_Expo(M, e, N))
main()

