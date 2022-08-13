rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
grafix = [rock,paper,scissors]
names = ["rock","paper","scissors"]

pl_choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n"))
print(f"You chose {names[pl_choice]}")
print(grafix[pl_choice])


com_choice = random.randint(0,2)
print(f"Computer chose {names[com_choice]}")
print(grafix[com_choice])

win = 0
if com_choice==0 and pl_choice==2:
  win = 2
if com_choice==2 and pl_choice==0:
  win=1
if com_choice==1 and pl_choice==0:
  win = 2
if com_choice==0 and pl_choice==1:
  win=1
if com_choice==2 and pl_choice==1:
  win=2
if com_choice==1 and pl_choice==2:
  win=1
if win == 0:
  print('Tie')
elif win == 1:
  print('You win!')
else:
  print('You lose :(')