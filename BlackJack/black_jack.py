import art
#import replit
import random

def has_ace(deck):
  if 11 in deck and 1 not in deck and sum(deck)>21:
    deck[deck.index(11)] = 1
    print("Deck changed")
  return deck
    
    
  
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
name = input("What is your name: ").title()
ans = input("Do you want a game of blackjack? Type 'y' or 'n': ")
while ans == 'y':
  replit.clear()
  print(art.logo)
  users_hand = []
  pcs_hand = []
  users_hand.append(random.choice(cards))
  users_hand.append(random.choice(cards))
  users_hand = has_ace(users_hand)

  print(f"Your hand is {users_hand} is total: {sum(users_hand)}")
  pcs_hand.append(random.choice(cards))
  print(f"Computer's hand is {pcs_hand}")
  pcs_hand.append(random.choice(cards))
  pcs_hand = has_ace(pcs_hand)

  gameover = False
  if (sum(pcs_hand) == 21):
    print("Computer has a blackjack, you lose!")
    gameover = True
  elif (sum(users_hand) ==21):
    print(f"{name} has a blackjack")
    gameover = True
  else:
    card = input("Do you want another card? ")
    while card != "n" and sum(users_hand) <= 21 and gameover == False:
      users_hand.append(random.choice(cards)) 
      users_hand = has_ace(users_hand)
      print(f"Your hand is {users_hand} is total: {sum(users_hand)}")
      if sum(users_hand) >=21:
        gameover = True
      else:
        card = input("Do you want another card? ")
    while gameover == False and sum(pcs_hand) <16 and sum(pcs_hand) <=21:
        pcs_hand.append(random.choice(cards))
        pcs_hand = has_ace(pcs_hand)

        
    print(f"Computer's hand is {pcs_hand} with total: {sum(pcs_hand)}")
    if sum(users_hand)>21:
      if sum(pcs_hand)>21:
        print("Draw!")
      else:
        print("Computer wins!")
    elif sum(pcs_hand)>21:
        print(f"{name} wins!")
    else:
      if sum(pcs_hand) > sum(users_hand):
        print("Computer wins!")
      elif sum(pcs_hand) < sum(users_hand):
        print(f"{name} wins!")
      else:
        print("Draw!")
    
  ans = input("Do you want a game of blackjack? Type 'y' or 'n': ")