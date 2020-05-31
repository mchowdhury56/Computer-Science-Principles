from cs115 import *

def dot (L, K):
    '''gives the dot product of lists L and K'''
    if L == []:
        return 0.0
    elif K == []:
        return 0.0
    else:
        return L[0]*K[0] + dot (L[1:],K[1:])

def explode(S):
    '''takes a string S and returns it as a list of characters'''
    if S == (''):
        return []
    else:
        return [S[0]]+ explode (S[1:])

def ind (e, L):
    '''takes an element e and a sequence L and returns the index when e if first found in L'''
    if L == [] or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind (e,L[1:])

def removeAll (e,L):
    '''takes an element e and a sequence L and returns L with e removed'''
    if L == []:
        return []
    elif L[0] == e:
        return [L[1]] + removeAll(e, L[2:])
    else:
        return [L[0]] + removeAll(e, L[1:])
    
def myFilter (f, L):
    '''returns a new list L after testing function f '''
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])

def deepReverse (L):
    '''takes a list L and returns the reversal of the list'''
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
