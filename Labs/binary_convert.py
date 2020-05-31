from cs115 import*
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    if isOdd(n) == True:
        return (numToBinary(n//2) + "1" )
    else:
        return (numToBinary(n//2) + "0")

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    if s[-1] == 0:  return 0
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    newbinary = numToBinary(binaryToNum(s)+1)
    if s == '11111111': return '00000000'
    else:
        if len(newbinary) < 8:
            n= 8-len(newbinary)
            return n*'0' + newbinary
        else:   return newbinary

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print (s)
    if n == 0:  return None
    else:   return count(increment(s),n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif n//3 == 0: return str(n%3)
    else:
        return numToTernary(n//3) + str(n%3)
        

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    if s[-1] == 0:  return 0
    else:
        return 3 * ternaryToNum(s[:-1]) + int(s[-1])
