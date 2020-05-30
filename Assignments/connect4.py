class Board:
    ''' class for the connect 4 board'''

    def __init__(self, width=7, height=6):
        ''' contructor for the board'''
        self.columns = width
        self.rows = height
        self.board = []
        for row in range(self.rows):
            rows = []
            for col in range(self.columns):
                rows += [' ']
            self.board.append(rows)
                
                
    def __str__(self):
        '''returns a representation of the connect 4 board'''
        board = ''
        for row in self.board:
            board += '|'
            for col in row:
                board += col + '|'
            board += '\n'
        board += self.columns * "--" + "-\n"
        board += " "
        for spaces in range(self.columns):
            board += str(spaces) + " "
        return board
                
        

    def allowsMove(self, col):
        ''' returns true if there is space in the column to make a move or
        false if there is no space available or if the column is invalid'''
        if col < 0 or col > self.columns - 1:
            return False
        if self.board[0][col] != ' ':
            return False
        return True

    def addMove(self, col, ox):
        '''ox checker where ox is a variable holding a string that is
            either "X" or "O", into column'''
        for row in range(len(self.board)-1,-1,-1):
            if self.board[row][col] == ' ':
                    self.board[row][col] = ox
                    break

    def setBoard( self, moveString ):
        ''' takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers '''
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.columns:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def delMove(self,col):
        ''' removes the top checker from the column col. If the column
            is empty, then do nothing'''
        for row in range(len(self.board)):
            if self.board[row][col] != ' ':
                self.board[row][col] = ' '
                break

    def winsFor(self, ox):
        '''returns True if the given checker, 'X' or 'O', held in ox,
            has won the calling Board. Returns False otherwise.'''
        for row in range(self.rows): #Horizontal
            for col in range(self.columns):
                if((col+3) < self.columns):
                    if ox == self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                        return True
        for row in range(self.rows): #Vertical
            for col in range(self.columns):
                if((row+3) < self.rows):
                    if ox == self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                        return True
        for row in range(self.rows): #Diagonal 1
            for col in range(self.columns):
                if((col+3) < self.columns) and ((row+3) < self.rows):
                    if ox == self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                        return True
        for row in range(self.rows): #Diagonal 2
            for col in range(self.columns):
                if((col+3) < self.columns) and ((row+3) >= 0):
                    if ox == self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
                        return True
        return False

    def hostGame( self ):
        '''runs a loop to allow users to play a game'''
        print('Welcome to Connect Four!')
        print(self)
        def Xturn(self,ox):
            ox = 'X'
            try:
                Xchoice = int(input("X's choice: "))
                if self.allowsMove(Xchoice) == True:
                    self.addMove(Xchoice, ox)
                    print(self)
                else:
                    print('Please make a valid move.')
                    Xturn(self,ox)
            except ValueError:
                print('Please enter a number between 0 and 1 less than the numbner of columns')
                Xturn(self,ox)

        def Oturn(self,ox):
            ox = 'O'
            try:
                Ochoice = int(input("O's choice: "))
                if self.allowsMove(Ochoice) == True:
                    self.addMove(Ochoice, ox)
                    print(self)
                else:
                    print('Please make a valid move.')
                    Oturn(self,ox)
            except ValueError:
                print('Please enter a number between 0 and 1 less than the number of columns')
                Oturn(self,ox)

        while True:
            ox = 'X'
            Xturn(self,ox)
            if all(self.allowsMove(col) == False for col in range(self.columns)):
                print('This game is a tie. Please start a new game.')
                return
            if self.winsFor(ox) == True:
                break
            ox = 'O'
            Oturn(self,ox)
            if all(self.allowsMove(col) == False for col in range(self.columns)):
                print('This game is a tie. Please start a new game.')
                return
            if self.winsFor(ox) == True:
                break
        print(ox + " wins -- Congratulations!")
        print(self)

