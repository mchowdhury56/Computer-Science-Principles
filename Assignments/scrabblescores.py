import sys
from cs115 import *

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def ind (e, L):
    '''takes an element e and a sequence L and returns the index when e if first found in L'''
    if L == [] or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind (e,L[1:])
    
def letterScore (letter, scorelist):
    '''returns the value associated with the letter in scrabbleScores list'''
    return filter(lambda scorecard: letter==scorecard[0], scorelist)[0][1]

def wordScore (S,scorelist):
    '''returns the scrabble score of a string'''
    if S == '' or S == []:
        return 0
    else:
        return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def scoreList (Rack):
    '''takes a list of lowercase letters "Rack" and returns all the word
combinations that can be made with the letters and each word's scrabble score'''
    def possibleWords(newRack,Word):
        if Word == '':
            return True
        elif Word[0] in newRack:
            return possibleWords(newRack[0:ind(Word[0],newRack)]
                                 +newRack[ind (Word[0],newRack)+1:], Word[1:])
        else:
            return False

    usable = filter(lambda y: possibleWords(Rack,y),Dictionary)
    newlist = map(lambda x:[x,wordScore(x,scrabbleScores)],usable)
    return newlist

def bestWord(Rack):
    '''Returns the word the highest score that can be made with letters in the
Rack according to the dictionary along with its scrabblescore'''
    def highestScore (x,y):
            if x[1]>y[1]:
                return x
            else:
                return y
    if scoreList (Rack) == []:
        return ['',0]
    else:
        return reduce(highestScore,scoreList (Rack))

    

