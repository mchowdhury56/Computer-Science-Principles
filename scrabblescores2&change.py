from cs115 import *
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(amount,coins):
    '''returns a list with the minimun number of coins needed and a list of
        the coins used to get that number of coins'''
    lastCoin = len(coins) - 1
    if amount == 0: return [0,[]]
    elif coins == []: return [float("inf"),[]]
    else: #we have an amount and list of coin values
        if coins[lastCoin] > amount: #if biggest coin> amount we dont need it
            return giveChange(amount,coins[0:lastCoin])
        else:
            use = giveChange(amount-coins[lastCoin], coins)
            lose = giveChange(amount,coins[0:lastCoin])
            if use[0]>lose[0]:
                return lose
            else: return [1+use[0],use[1]+[coins[lastCoin]]]

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore (letter, scorelist):
        return filter(lambda scorecard: letter==scorecard[0], scorelist)[0][1]

    def wordScore (S,scorelist):
        if S == '' or S == []:
            return 0
        else:
            return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)
    if dct == []:   return []
    else:
        newlist = map(lambda x:[x,wordScore(x,scores)],dct)
        return newlist



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    def slicer(acc,n,L):
        if n == 0:   return acc
        else:   return slicer(acc+[L[0]],n-1,L[1:])
    return slicer([],n,L)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n==0:    return L
    elif L==[]:    return []
    else:
        return drop(n-1,L[1:])


