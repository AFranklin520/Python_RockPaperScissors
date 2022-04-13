# FranklinP5
# Programmer: Anthony Franklin
# Email: afranklin18@cnm.edu
# Purpose: provides user capability to play rock scissor paper

import random
choices=("Rock","Paper","Scissors")
winner={"Rock":"Scissors","Paper":"Rock","Scissors":"Paper"}
intro='Rock, Paper, Scissors'
hw=0
cw=0
t=0
x=input('Wanna play a game??? (Y/N) :')
ht=0
ct=0
games=0

play=True
while True:
    if x.lower()=='y':
        print(intro)
        text_width =len(intro)
        screen_width=80
        box_width=text_width+6
        left_margin=(screen_width-box_width)//2
        print(' '*left_margin+'*'*text_width)
        print(' '*left_margin+intro)
        print(' '*left_margin+'*'*text_width)
        print('\n\nRULES: Best of 3 wins the round.\n')
        break
    else:
        print('Adios then!')
        exit()

while play:
    humanchoice=input("Choose Rock, Paper, or Scissors :").title()
    compchoice=choices[random.randrange(3)]
    print("Computer chose:",compchoice)
    print("You chose:",humanchoice)
    if winner[humanchoice]==compchoice:
        victor="You"
        hw +=1
    elif winner[compchoice]==humanchoice:
        victor="Computer"
        cw +=1
    else:
        victor="a Tie"
        t +=1
    print('The winner of this round is {}'.format(victor))
    if (hw <3)and(cw <3)and (t<3):
        print('The score after this round is \nYou: {},\nThe Computer: {}, \nTies: {}\n'.format(hw,cw,t))
    elif hw==3:
        print("You win!!\n")
        ht +=1
        games +=1
        hw=0
        cw=0
        t=0
        print('The score after {} games is\n You: {}\n Computer: {}\n'.format(games,ht, ct))
    elif cw==3:
        print("Sorry, the computer won this time! Get good noob!!\n")
        ct +=1
        games +=1
        hw=0
        cw=0
        t=0
        print('The score after {} games is\n You: {}\n Computer: {}\n'.format(games,ht,ct))
    else:
        print("Sorry, ties don't count!\n")
        hw=0
        games +=1
        cw=0
        t=0
        print('The score after {} games is\n You: {}\n Computer: {}\n'.format(games,ht,ct))
    again=input("\nWant to play again? (Y/N) :")
    if again.lower()!='y':
        play=False
        print("Thanks for playing with me. The final score was \nYou: {}\nComputer: {}\nRounds played: {}\n\n Goodbye".format(ht,ct,games))
    else:
        play=True

    
