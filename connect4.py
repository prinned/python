import re, itertools

class player:
    tot=0
    length=6
    table=[['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' '],
           ['_', ' ', ' ', ' ', ' ', ' ']]
    last_player=0

    def __init__(self,symbol):
        if player.tot > 2:
            print("Error! Too many players!")
            return

        if symbol==' ' or symbol=='' or symbol=='_':
            print("Invalid symbol!")

        player.tot+=1
        self.symbol=symbol
        self.pin=player.tot
        print('You are Player No. ',self.pin,'!',sep='')

        if player.tot==2:
            print("It's your turn, Player 1!")
    
    def display(self=None):
        for horiz in range(5,-1,-1):
            print('|',sep='',end='')
            [print(player.table[colno][horiz],'|',sep='',end='') for colno in range(7)]
            print()
        print("|1|2|3|4|5|6|7|\n")

    def play(self,col):
        if player.table[col][5] != ' ':
            print('Error! Full!')
            return

        for i in [4,3,2,1,0]:
            if player.table[col][i]!=' ' and player.table[col][i]!='_': #if i^th place is full:
                player.table[col][i+1]=self.symbol
                self.display()
                return
        
        #if everything is empty:
        player.table[col][0]=self.symbol
        print(player.table)
        self.display()

    def check_for_win(self):
        #column win
        [print('Player',self.pin,"has won!") for i in range(7) if ''.join([self.symbol]*4) in ''.join(player.table[i])]
        #row win
        [print('Player',self.pin,"has won!") for rowno in range(6) if ''.join([self.symbol]*4) in ''.join([player.table[colno][rowno] for colno in range(7)])]
        #forward diagnol win: /
        def fdiag_set(col,row):
            ret=[player.table[col][row]]
            while col < 7 and row < 6:
                ret.append(player.table[col][row])
                col+=1
                row+=1
            return ret

        for i in fdiag_set(1,0):
            i='Z'



chk=player('X')
chk2=player('Y')
chk.play(6)
chk2.play(4)
chk.check_for_win()
chk.display()