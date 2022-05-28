import os
from colorama import Fore as color
from time import sleep as wait
from random import randint
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
finchance = None
per = 100
trap = 25
lg = 0
tg = 0
p = 0

print("Hello!")
print("Please Read the how_to_play.md before playing.")
while True:
    legendchance = 0
    trapchance = 0
    c = cpc + gr
    print(color.GREEN + "~~~~~~ Emoji Clicker ~~~~~~")
    print(color.RESET + "Please choose your action:")
    print('[ENTER] Click Once')
    print('1: Shop   2: Settings')
    print('3: Stats  4: Leaderboard')
    print('5: Exit')
    print(f"You now have {emoji} Emojis")
    q = input('Action: ')
    if q == '':
       trapchance = randint(1,trap)
       print(f"You clicked once {emo}")
       if tr == True:
          legendchance = randint(1,per)
       if trapchance == 25:
            tenper = emoji / 10
            emoji -= tenper
       elif legendchance == per:
            emoji += 1000
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
       print("10: Decrease Trap Chance by 1%")
       print("11: Increase Legendary Emoji Chance by 1%")
       print("12: Emoji Party …… Increase Emoji Per Click by 100000 --- $3499999")
       print("13: Emoji House …… Increase Emoji Per Click by 2500000 --- $77777777")
       print("14: Emoji Town …… Increase Emoji Per Click by 20000000 --- $499999999")
       print("15: Paradise or Hell? …… Gets 0~10000000000 Emojis --- $300000000")
       print("16: ??? …… 00010101010100101010101001 --- $10110010001")
       print("17: Dont buy! …… This is dangerous.I’m warning you. --- $999999999999")
       print("18: Go Back")
       x = input("Want to buy: ")
       if x == '1':
          if emoji >= pri:
             gr += 1
             emo = new
             new = nlis[gr]
          else:
             warn()
       elif x == '2':
            p = 96
            ac = 1
       elif x == '3':
            p = 899
            ac = 10
       elif x == '4':
            if emoji >= 1198:
               emoji -= 1198
               emoji += randint(0,3000)
       elif x == '5':
