from cs115 import*

def numToBaseB(N,B):
    ''' takes an integer n and gives the base b representation of it'''
    if N==0:
        return '0'
    elif N//B == 0: return str(N%B)
    else:
        return numToBaseB(N//B,B) + str(N%B)
def baseBToNum(S,B):
    ''' takes a string s in base b and gives the integer value of the string in base 10'''
    if S == '': return 0
    if S[-1] == 0:  return 0
    else:
        return B * baseBToNum(S[:-1],B) + int(S[-1])
def baseToBase(B1,B2,SinB1):
    ''' takes a string in base b1 and gives the base b2 reprsentation of it'''
    return numToBaseB(baseBToNum(SinB1,B1),B2)
def add(S,T):
    ''' takes two binary strings s and t and gives the sum of them in binary
    converts the strungs to base 10 adds them and converts it back to binary'''
    x = int(baseToBase(2,10,S))
    y = int(baseToBase(2,10,T))
    z = x+y
    return numToBaseB(z,2)

FullAdder ={('0','0','0') : ('0','0'),
            ('0','0','1') : ('1','0'),
            ('0','1','0') : ('1','0'),
            ('0','1','1') : ('0','1'),
            ('1','0','0') : ('1','0'),
            ('1','0','1') : ('0','1'),
            ('1','1','0') : ('0','1'),
            ('1','1','1') : ('1','1')}

def zeroremover(x):
    '''Removes leading zeros in a string'''
    if x == '0': return x
    elif x[0] != '0': return x
    else: return zeroremover(x[1:])
    
def addB(S,T):
    '''add two binary strings together in a different and more direct way'''
    if len(S) > len(T):
        T = '0' * (len(S)-len(T)) + T
    if len(T) > len(S):
        S = '0' * (len(T)-len(S)) + S
    def addB_helper(S,T,C):
        '''uses FullAdder to add the binary terms from right to left'''
        if S == '': return C
        else:
            x = S[-1]
            y = T[-1]
            total = FullAdder[(x,y,C)]
            return addB_helper(S[:-1],T[:-1],total[1]) + total[0]
    return zeroremover(addB_helper(S,T,'0'))
