# Good Luck reading all this
# Wait, Do not scroll down!
# There's a secret!

import os
from colorama import Fore as color
from time import sleep as wait
from random import randint
from discord.ext import tasks
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
    try:
      raise SyntaxError("Not Enough Money.")
    except:
      print(color.RED + "Not Enough Money.")
            
def invalid():
    print(color.RED + "Invalid Input" + color.RESET + '.')
    wait(2)
    
# Game Start
print("Hello!")
print("Please Read the README.md before playing.")
while True:
    legendchance = 0
    trapchance = 0
    c = cpc + gr + 1
    print(color.GREEN + "~~~~~~ Emoji Clicker ~~~~~~")
    print(color.RESET + "Please choose your action:")
    print('[ENTER] Click Once')
    # Choose Action Code
    print('1: Shop   2: Settings')
    print('3: Stats  4: Leaderboard')
    print('5: Pause  6: Exit')
    print(f"You now have {emoji} Emojis")
    if gamefin == True:
       print(color.CYAN + "You finished the game!")
       print("Congratulations!")
       print("Keep playing!" + color.RESET)
    q = input('Action: ')
    if q == '':
       trapchance = randint(1,trap)
       print(f"You clicked once {emo}")
       if tr == True:
          legendchance = randint(1,per)
       if trapchance == 25:
            if trapd == False:
               tenper = emoji / 10
               emoji -= tenper
               print("Oh no! This is a trap!")
               wait(3)
       elif legendchance == per:
            emoji += c * 69
            print("Legend……")
            wait(2)
       else:
            emoji += c
       clicks += 1
    elif q == '1':
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
       up = False
       l = 0
       note = False
       add = True
       s = None
       ss = None
       trapdd = False
       if x == '1':
            ss = f" Congrats you upgraded!"
            p = pri
            up = True
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
                 if s == None:
                   print(ss)
                   wait(3)
                 elif ss == None:
                   pass
                 else:
                   print(f"Congrats you bought a/an {s}!")
                   wait(3)
                 emoji -= p
                 if ac > 0:
                      cpc += ac
                 emoji += add
                 if trapdd == True:
                      trapd = True
                 if det > 0:
                      trap += det
                 if inl > 0:
                      per -= inl
                 if l == True:
                      tr = True
                 if w == True:
                      gamefin = True
                 if up == True:
                   if gr != 10:
                      gr += 1
                      emo = new
                      new = nlis[gr]
                      pri = pri*3
            else:
                 note = True
            if note == True:
                 warn()
                 wait(3)
       else:
            pass
    elif q == '2':
        print("Will publish in v1.3!")
    elif q == '3':
        os.system('clear')
        print("~~~~~~~Your Stats~~~~~~~")
        print(f"Emojis: {emoji}  Emojis Per Click: {c}")
        print(f"Chance of finding a Legendary Emoji: 1/{per}")
        print(f"Chance of finding a trap: 1/{trap}")
        print(f"Game Finished: {gamefin}  Total Clicks: {clicks}")
        print(f"Current Emoji: {emo}  Emoji Grade: {gr}")
        wait(5)
    elif q == '4':
        print("Will publish in v2.0!")
    elif q == '5':
        os.system('clear')
        print("Game Paused")
        print("Type anything to continue")
        reply = input("Reply: ")
    if q == '6':
        print(color.RED + "You will lose all your progress.")
        print("Are you sure want to exit?")
        print("Type 999 to exit, anything else to cancel.")
        leave = input("Answer: ")
        if leave == '999':
          raise NameError("Game Over.")
        else:
           print(color.RESET + "Action Cancelled.")
           wait(3)
    else:
        warn()
    os.system('clear')

    
    
    
    
# Leave 










# Stop now









































# You will regret this




































# Back to the top





































# Stop buddy








"""
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
(Oooooooh, Give you up
Oooooooh, Give you UP)
Never gonna give, never gonna give (Always gonna take, always gonna take)
(Give you up)
Never gonna give, never gonna give (Always gonna take, always gonna take)
(Give you up)
We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""
# Get rickrolled for being down here
