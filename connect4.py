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
        if player.tot > 1:
            print("Error! Too many players!")
            return

        if symbol==' ' or symbol=='' or symbol=='_': print("Invalid symbol!")

        player.tot+=1
        self.symbol=symbol
        self.pin=player.tot
        print('You are Player No. ',self.pin,'!',sep='')

        if player.tot==2: 
            print("It's your turn, Player 1!")
            player.display()
    
    def display(self=None):
        for horiz in range(5,-1,-1):
            print('|',sep='',end='')
            [print(player.table[colno][horiz],'|',sep='',end='') for colno in range(7)]
            print()
        print("|1|2|3|4|5|6|7|\n")

    def play(self,col):
        col-=1
        try:
            if player.table[col][5] != ' ':
                print('Error! Full!')
                return
        except IndexError:
            print('Invalid Column!')
            return

        if player.last_player==self.pin:
            print('It\'s not your turn yet!')
            return

        player.last_player = self.pin
        for i in [4,3,2,1,0]:
            if player.table[col][i]!=' ' and player.table[col][i]!='_': #if i^th place is full:
                player.table[col][i+1]=self.symbol
                if self.check_for_win():
                    print('Player',self.pin,'has won!')
                    for j in range(7):
                        if player.table[j][5] == ' ':
                            player.table[j][5]='!'
                self.display()
                return
        
        #if everything is empty:
        player.table[col][0]=self.symbol
        if self.check_for_win():
                    print('Player',self.pin,'has won!')
                    for i in range(7):
                        if player.table[i][5] != ' ':
                            player.table[i][5]='!'
        self.display()
                        

    def fdiag(col,row):
        ret=[player.table[col][row]]
        while col < 7 and row < 6:
            ret.append(player.table[col][row])
            col+=1
            row+=1
        return ''.join(ret)
            
    def bdiag(col,row):
        ret=[player.table[col][row]]
        while col > -1 and row < 6:
            ret.append(player.table[col][row])
            col-=1
            row+=1
        return ''.join(ret)
        

    def check_for_win(self):
        chk=False
        #column win
        for i in range(7):
            if ''.join([self.symbol]*4) in ''.join(player.table[i]):
                chk = True
        #row win
        for rowno in range(6):
            if ''.join([self.symbol]*4) in ''.join([player.table[colno][rowno] for colno in range(7)]):
                chk = True
        #forward diagnol win: /
        
        if (self.symbol*4 in player.fdiag(1,0) or
            self.symbol*4 in player.fdiag(0,0) or
            self.symbol*4 in player.fdiag(0,1) or
            self.symbol*4 in player.fdiag(0,2) or
            self.symbol*4 in player.fdiag(2,0) or
            self.symbol*4 in player.fdiag(3,0)):
            chk=True

        #backward diagnol win: \ 
        
        if (self.symbol*4 in player.bdiag(6,0) or
            self.symbol*4 in player.bdiag(6,1) or
            self.symbol*4 in player.bdiag(6,2) or
            self.symbol*4 in player.bdiag(5,0) or
            self.symbol*4 in player.bdiag(4,0) or
            self.symbol*4 in player.bdiag(3,0)):
            chk=True

        return chk
        


if __name__=='__main__':
    p1=player('X')
    p2=player('O')
    while True:
        x=input('>>')
        try:
            exec(x)
        except Exception as e:
            print("Error!",Exception)

