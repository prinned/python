'''
Program to play single player hangman with computer generated words.
Online text file the words came from: https://raw.githubusercontent.com/paritytech/wordlist/master/res/wordlist.txt
Art made by yours truly! 
'''

import functools, string, re, random, requests

class hang:
    website='https://raw.githubusercontent.com/paritytech/wordlist/master/res/wordlist.txt'

    
    man=['\n\n\n\n\n\n\n\n\n',
         '\n ___________\n|\n|\n|\n|\n|\n|\n\n',
         '\n ___________\n|           |\n|           |\n|           |\n|           |\n|           |\n|___________|\n',
         '\n ___________\n|     |     |\n|           |\n|           |\n|           |\n|           |\n|___________|\n',
         '\n ___________\n|     |     |\n|     0     |\n|           |\n|           |\n|           |\n|___________|\n',
         '\n ___________\n|     |     |\n|     0     |\n|     |     |\n|           |\n|           |\n|___________|\n',
         '\n ___________\n|     |     |\n|     0     |\n|     |     |\n|    / \\    |\n|           |\n|___________|\n',
         '\n ___________\n|     |     |\n|    \\0/    |\n|     |     |\n|    / \\    |\n|           |\n|___________|\n',
         '\n ___________\n| | | | | | |\n| | |\\0/| | |\n| | | | | | |\n| | |/|\\| | |\n| | | | | | |\n|_|_|_|_|_|_|\n',
         '\n ___________\n| | | | | | |\n| | |\\0/| | |       Gregory is forever forgotten.\n| | | | | | |       His wife wrongly believes he was a  \n| | |/|\\| | |       traitor from the start yet never \n| | | | | | |       moves on.\n|_|_|_|_|_|_|\n',
         '\n     _\n  0 /0\\  Gregor thanks you for \n /|\\/|\\  uniting him with his wife!\n  |  Δ   They live happily\n / \\/ \\  ever after!\n']
        
    hide=lambda word, hints: re.sub(("[^"+functools.reduce(lambda a,b:a+b, hints)+"]"), '_', word)
    
    def __init__(self=None):
        print('Accessing online directory... (May take up to a minute)')
        global word_list
        word_list=requests.get(hang.website).text.splitlines()
        print('Success!')
        
    def mword(self=None):
        length=1
        while length<4:
            hang.word=random.choice(word_list).lower()
            length=len(hang.word)

        global hints
        hints = [random.choice(string.ascii_lowercase) for i in range(len(hang.word)//4+1)]

        i=0
        while i <len(hints):     #checks if the hint is in the word
            if not hints[i] in hang.word:
                hints[i]=random.choice(string.ascii_lowercase)
                i-=1
            i+=1
        
        hang.hid = hang.hide(hang.word,hints)

    def guess(self=None):
        ihint=hints
        guessed=[]
        i=0
        while i<8:
            print(hang.man[i])
            print(hang.hid.replace("", " ")[1: -1]) #[1:-1] to skip the first character
            x=input("Enter your guess: ")
            if len(x)>1:
                print("Word guess!")
            if x=='':
                continue
            elif x in ihint:
                print('That was the hint! Pay attention!')
            elif x in guessed:
                print("You've already guessed that, dummy!")
                continue
            elif x in hang.word:
                hints.append(x)
                hang.hid = hang.hide(hang.word,hints)
                print('Correct!')
                guessed.append(x)
                if hang.hid==hang.word:
                    print("You've won!")
                    print(hang.man[10])
                    del i
                    break
            else: 
                print('Wrong!')
                i+=1
                guessed.append(x)
                if i==8:
                    print(hang.man[9])
                    print('Greogory is dead thanks to you.')
                    del i
                    print('It was', hang.word)
                    break


if __name__=="__main__":
    hang()       
    x='y'
    while x=='y':       
        hang.mword()
        hang.guess()
        x=input('Reset? (y/n) ').lower()