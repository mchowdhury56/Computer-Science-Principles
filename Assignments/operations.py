
from cs115 import*

def mult (x,y):
    return x * y

def add (x,y):
    return x + y

def divide (x,y):
    return x/y

def divides(n):
    def div(k):
        return n % k == 0
    return div

'''factorial function'''

def factorial (n):
    '''returns n!'''
    list1 = range (1,n+1)
    return reduce (mult, list1)

'''mean function'''

def mean (L):
    '''returns the mean of a list of numbers L'''
    total = reduce (add,L)
    return divide (total,len (L))

'''prime function'''
def prime (n):
    '''determines whether a number n is prime or composite
       True=Prime False=Composite'''
    if True in map (divides (n),range (2,n)):
        return False
    return True
    
    

