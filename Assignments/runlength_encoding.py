# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%2 == 0:
        return numToBinary(n/2) + "0"
    elif n%2 == 1:
        return numToBinary(n//2) + "1"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + 2*binaryToNum(s[:-1])

def binaryPadded(n):
    '''Pads zeros in front of the binary string for a specific length.'''
    s = numToBinary(int(n))
    return "0"*(COMPRESSED_BLOCK_SIZE - len(s)) + s

def prefixLength(s):
    '''Returns the padded value of a string'''
    if len(s) == 1:
        return 1
    if s[0] != s[1]:
        return 1
    return 1 + prefixLength(s[1:])

def compress(S):
    '''returns a run-length encoding of the 64 bit input string.'''
    def compress_help(S,x):
        if S == "":
            return ""
        if S[0] != chr(x+ord("0")):
            return binaryPadded("0") + compress_help(S,1-x)
        else:
            length = prefixLength(S)
            length = min(length,MAX_RUN_LENGTH)
            return binaryPadded(length)+compress_help(S[length:],1-x)
    return compress_help(S,0)


def uncompress(C):
    '''returns an inversion or undoing the compressed string.'''
    if C == "":
        return ""
    if len(C) == COMPRESSED_BLOCK_SIZE:
        return binaryToNum(C)*"0"
    else:
        return binaryToNum(C[0:5])*"0" + binaryToNum(C[5:10])*"1" + uncompress(C[10:])
    
def compression(S):
    '''gives the ratio of the compress string to the uncompressed string'''
    if len(S) == 0:
        return
    return  len(compress(S)) / len(S)

'''The maxiumum number of bits that the compress function can use is 325 because a string
with alternating 0s and 1s starting with 1 would be represented with 00000 and then 00001 64 times'''
'''We conducted tests for our compress, uncompress, and compression functions by running the
functions with the test "images" as the input. We found the compression ratio of the penguin
to be 1.484375, the smile to be 1.328125, and the five to be 1.015625'''
'''There is no algorithm possible that can exist to what Professor Lai claims his can do. This is
because his compressed bit would be less than a value that can hold 64 bits, so 63 or lower. It is
basically saying like he can store all of the different possible combinations of data a 64 bit string, which is
2^64, into a string that can hold up to half as many combinations(2^63). This is not mathamatically possible.'''
