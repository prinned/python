class player:
    r=[[' ',' ',' '],
       [' ',' ',' '],
       [' ',' ',' ']]
    pni=1
    global rp
    
    def __init__(self, symbol):
        self.symbol=symbol

        if symbol == ' ':
            print('Error! Invalid symbol! Please choose another one.')
            return
        
        if player.pni >2:
            print('Error! Too many players!')
            self.symbol=' '
            return

        self.pin=player.pni
        print('You are Player ', self.pin,'!',sep='')

        if player.pni==2:
            print('Good Luck, both of you! Your turn, Player 1!')
            player.display()

        player.pni+=1

    def display():
        print(0,'|', player.r[0][0], player.r[0][1], player.r[0][2])
        print(1,'|', player.r[1][0], player.r[1][1], player.r[1][2])
        print(2,'|', player.r[2][0], player.r[2][1], player.r[2][2], '', sep='_')
        print('  | 0 1 2')
        
        #checking for win
        #sleeping win
        if ((player.r[0][0] == player.r[0][1] and player.r[0][1] == player.r[0][2] and player.r[0][0]!=' ') or 
            (player.r[1][0] == player.r[1][1] and player.r[1][1] == player.r[1][2] and player.r[1][0]!=' ') or 
            (player.r[2][0] == player.r[2][1] and player.r[2][1] == player.r[2][2] and player.r[2][0]!=' ')):
            print('\n',rp.symbol,' has WON! Press Enter to Close.',sep="")
            d=input()
            close=True
            
        
        #standing win
        elif ((player.r[0][0] == player.r[1][0] and player.r[0][0] == player.r[2][0] and player.r[0][0]!=' ') or 
              (player.r[0][1] == player.r[1][1] and player.r[0][1] == player.r[2][1] and player.r[0][1]!=' ') or 
              (player.r[0][2] == player.r[1][2] and player.r[0][2] == player.r[2][2] and player.r[0][2]!=' ')):
            print('\n',rp.symbol,' has WON! Press Enter to Close.',sep="")
            d=input()
            close=True
            
        #diagnol win
        elif ((player.r[0][0] == player.r[1][1] and player.r[0][0] == player.r[2][2] and player.r[0][0]!=' ') or 
              (player.r[0][2] == player.r[1][1] and player.r[0][2] == player.r[2][0] and player.r[0][2]!=' ')):
            print('\n',rp.symbol,' has WON! Press Enter to Close.',sep="")
            d=input()
            close=True

        #draw
        for i in player.r:
            if ' ' in i:
                return
        d=input('DRAW! Press Enter to Close.')
        close=True
        

    def play(self, x, y):
        if player.pni <3:
            print('You can\'t play alone, silly! Get a friend!')
            return
        
        if player.r[x][y] != ' ':
            print("That move's already been played, ", self.symbol,"!",sep="")
            return
        
        global rp
        try:
            if rp==self:
                print('Its not your turn, ',self.symbol,'!',sep='')
                return
        except:
            if self.pin!=1:
                print('Its not your turn, ',self.symbol,'!',sep='')
                return
        rp=self
        
        player.r[x][y]= self.symbol
        player.display()
    
    def restart(self):
        r=[[' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' ']]
        pni=1
        global rp
        del self.symbol


if __name__=='__main__':
    player.display()
    type_of_display = input('Are you running this program directly or using an IDLE? (d for direct, i for IDLE) ')
    if type_of_display=='d':
        close=False
        while close==False:
            try:
                x= input('$ ')
                exec(x)
            except:
                print('Unexpected Error!')
