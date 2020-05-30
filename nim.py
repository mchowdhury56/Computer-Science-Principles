# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """

    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print('You win')
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print('I win')
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    try:
        pilenum = int(input('How many piles do you want to play with? '))
        while not (pilenum < 6 and pilenum > 0):  # want to play up to 5 piles
            print('Please enter a number between 1 and 5')
            pilenum = int(input('How many piles do you want to play with? '))
        num_piles = pilenum
        piles = [0] * pilenum
        for pile in range(num_piles):
            howMany = -1
            while not (howMany > 0):
                try:
                    howMany = int(
                        input('How many in pile ' + str(pile) + '? '))
                    if howMany <= 0 and num_piles >= 1:
                        print("The minimum coins needed for a pile is 1")
                except ValueError:
                    print("Error. Please enter a number")
            piles[pile] = howMany
    except ValueError:
        print("Error. Please enter a number between 1 and 5")
        init_piles()


def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    for pile in range(num_piles):
        print("pile  " + str(pile) + "  =  " + str(piles[pile]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles

    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    try:
        pnum = int(input('Which Pile? '))
        while not (pnum < num_piles and pnum >= 0):
            print('Please enter a number between 0 and 1 less than the number of piles')
            pnum = int(input('Which Pile? '))
        while not (piles[pnum] != 0):
            print('You cannot choose a pile that is empty. Please choose another pile')
            pnum = int(input('Which Pile? '))
        return pnum
    except ValueError:
        print("Error. Please enter a number between 0 and 1 less than the number of piles")
        get_pile()


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    try:
        howMany = int(input('How many? '))
        while not (howMany <= piles[pnum] and howMany > 0):
            print('Please enter a number between 1 and the number of coins in the pile')
            howMany = int(input('How many? '))
        return howMany
    except ValueError:
        print("Error. Please enter a number between 1 and the number of coins in the pile")
        get_number(pnum)


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    nimSum = piles[0]
    for each in range(1, num_piles):
        nimSum = nimSum ^ piles[each]
    return nimSum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    gameSum = game_nim_sum()
    for pile in range(num_piles):
        numberOfCoinsInPile = piles[pile]
        pileSum = gameSum ^ numberOfCoinsInPile
        if pileSum < numberOfCoinsInPile:
            return (pile, numberOfCoinsInPile - pileSum)
    for pile in range(num_piles):
        if piles[pile] > 0:
            return (pile, 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print('My turn ... ')
    play = opt_play()
    pileToTakeFrom = play[0]
    amountToTake = play[1]
    piles[pileToTakeFrom] -= amountToTake
    print('I remove ' + str(amountToTake) +
          ' from pile ' + str(pileToTakeFrom))


#   start playing automatically
if __name__ == "__main__":
    play_nim()
