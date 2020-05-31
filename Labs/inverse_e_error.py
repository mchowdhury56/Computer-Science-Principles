from cs115 import *
import math

def inverse (n) :
    '''returns reciprocal of n or 1/n'''
    return 1/n

def e(n) :
    '''approximates the value of e using Taylor expansion'''
    list1 = range (0, n+1)
    list2 = map (math.factorial, list1)
    list3 = map (inverse,list2)
    answer = sum (list3)
    return answer

    
def error(n) :
    '''returns difference between actual value of e and e(n)'''
    return abs(math.e-e(n))
