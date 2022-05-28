# Good Luck reading all this
# Wait, Do not scroll down!
# There's a secret!

import os
from colorama import Fore as color
from time import sleep as wait
from random import randint
# Variables Setting
cpc = 0
clicks = 0
emoji = 0
cps = 0

emo = '😶'
new = '🙂'
pri = 1200
inc = 10
gr = 0
nlis = ['😌','☺️','😊','😀','😄','😁','😆','🤩','🥳']

tr = False
legendchance = None
gamefin = False
per = 100
trap = 25
lg = 0
tg = 0
p = 0
trapd = False

# Functions
def warn():
    print(color.RED + 'Not enough Money.')
    
def invalid():
    print(color.RED + "Invalid Input" + color.RESET + '.')
    
# Game Start
print("Hello!")
print("Please Read the README.md before playing.")
while True:
    legendchance = 0
    trapchance = 0
    c = cpc + gr
    print(color.GREEN + "~~~~~~ Emoji Clicker ~~~~~~")
    print(color.RESET + "Please choose your action:")
    print('[ENTER] Click Once')
    # Choose Action Code
    print('1: Shop   2: Settings')
    print('3: Stats  4: Leaderboard')
    print('5: Pause  6: Exit')
    print(f"You now have {emoji} Emojis")
    q = input('Action: ')
    if gamefin = True:
       print(color.CYAN + "You finished the game!")
       print("Congratulations!")
       print("Keep playing!" + color.RESET)
    if q == '':
       trapchance = randint(1,trap)
       print(f"You clicked once {emo}")
       if tr == True:
          legendchance = randint(1,per)
       if trapchance == 25:
            if trapd = False
               tenper = emoji / 10
               emoji -= tenper
       elif legendchance == per:
            emoji += c * 69
       else:
            emoji += c
       clicks += 1
    if q == '1':
       os.system('clear')
       print("Choose your upgrade:")
       print(f"1: Upgrade your emoji to {new} and increase Emoji Per Click by {inc}. --- ${pri}")
       print("2: Emoji Mouse …… Increase Emoji Per Click by 1 --- $96")
       print("3: Emoji Keyboard …… Increase Emoji Per Click by 10 --- $899")
       print("4: Unknown Gift …… Gets 0~3000 emojis --- $1198")
       print("5: Emoji Document …… Increase Emoji Per Click by 50 --- $4199")
       print("6: Treasure Detector …… Will have 1% Chance of Finding a legend emoji  --- $5000")
       print("7: Emoji Fiction …… Increase Emoji Per Click by 400 --- $29999")
       print("8: Red Packet …… Gets 1000~50000 Emoji --- $32121")
       print("9: Emoji Bookshelf …… Increase Emoji Per Click by 6900 --- $339999")
       print("10: Decrease Trap Chance --- $694200")
       print("11: Increase Legendary Emoji Chance --- $999999")
       print("12: Emoji Party …… Increase Emoji Per Click by 100000 --- $3499999")
       print("13: Emoji House …… Increase Emoji Per Click by 2500000 --- $77777777")
       print("14: Emoji Town …… Increase Emoji Per Click by 20000000 --- $499999999")
       print("15: Paradise or Hell? …… Gets 0~10000000000 Emojis --- $300000000")
       print("16: ??? …… 00010101010100101010101001 --- $10110010001")
       print("17: Dont buy! …… This is dangerous.I’m warning you. --- $999999999999")
       print("18: Go Back")
       x = input("Want to buy: ")
       p = 0
       ac = 0
       add = 0
       w = 0
       det = 0
       inl = 0
       note = False
       add = True
       s = None
       ss = None
       trapdd = False
       if x == '1':
          if emoji >= pri:
             up = True
          else:
             note = True
       elif x == '2':
            p = 96
            ac = 1
            s = "Emoji Mouse"
       elif x == '3':
            p = 899
            ac = 10
            s = "Emoji Keyboard"
       elif x == '4':
            p = 1198
            add = randint(0,3000)
            ss = f"You got {add} emojis!"
       elif x == '5':
            p = 4199
            ac = 50
            s = "Emoji Document"
       elif x == '6':
            p = 5000
            l = True
            ss = "Congrats You unlocked Legend Emojis!"
       elif x == '7':
            p = 29999
            ac = 400
            s = "Emoji Fiction"
       elif x == '8':
            p = 32121
            add = randint(1000,50000)
            ss = f"You got {add} emojis!"
       elif x == '9':
            p = 339999
            ac = 6900
            s = "Emoji Bookshelf"
       elif x == '10':
            p = 694200
            det = 1
            ss = "Congrats You will have less chance of finding a trap!"
       elif x == '11':
            p = 999999
            inl = 1
            ss = "Congrats You will have more chance of finding a legendary emoji!"
       elif x == '12':
            p = 3499999
            ac = 100000
            s = "Emoji Party"
       elif x == '13':
            p = 77777777
            ac = 2500000
            s = "Emoji House"
       elif x == '14':
            p = 499999999
            ac = 20000000
            s = "Emoji Town"
       elif x == '15':
            p = 300000000
            add = randint(0,10000000000)
            ss = f"You got {add} Emojis!"
       elif x == '16':
            p = 10110010001
            trapdd = True
            ss = "What?! You delelted Traps system! The annoying traps will not appear again, Congrats!"
       elif x == '17':
            p = 999999999999
            w = True
            ss = "I told you not to buy……"
       elif x == '18':
            pass
       else:
            invalid()
       if p > 0:
            if emoji > p:
                 if s = None:
                   print(ss)
                 elif ss = None:
                   pass
                 else:
                   print(f"Congrats you bought a/an {s}!")
                 emoji -= p
                 if ac > 0:
                      cpc += ac
                 emoji += add
                 if trapdd = True:
                      trapd = True
                 if det > 0:
                      trap += det
                 if inl > 0:
                      per -= inl
                 if l == True:
                      tr = True
                 if w = True:
                      gamefin = True
             else:
                 note = True
             if up == True:
                 gr += 1
                 emo = new
                 new = nlis[gr]
             if note = True:
                 warn()
        else:
            pass
    if q == '2':
        print("Will publish in v1.3!")
    if q == '3':
        os.system('clear')
        print("~~~~~~~Your Stats~~~~~~~")
        print(f"Emojis: {emoji}  Emojis Per Click: {c}")
        print(f"Chance of finding a Legendary Emoji: 1/{per})
        print(f"Chance of finding a trap: 1/{trap})
        print(f"Game Finished: {gamefin}  Total Clicks: {clicks})
        print(f"Current Emoji: {emo}  Emoji Grade: {gr})
    if q == '4':
        print("Will publish in v2.0!")
    if q == '5':
        os.system('clear')
        print("Game Paused")
        print("Type anything to continue")
        reply = input("Reply: ")
    if q == '6':
        print(color.RED + "You will lose all your progress.")
        print("Are you sure want to exit?")
        print("Type 999 to exit, anything else to cancel.")
        leave = input("Answer: )
        if leave = '999':
           exit()
        else:
           print(color.RESET + "Action Cancelled.")
     os.system('clear')
