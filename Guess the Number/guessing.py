import art
import random
HARD_TRY = 5
EASY_TRY = 10
print(art.logo)
print("Welcome to the number guessing game!")
print("I am thinking of number between 1 and 100")
ans = input(" Choose difficulty, type 'easy' or 'hard': ").lower()
if ans == "easy":
    tries = EASY_TRY
else:
    tries = HARD_TRY
gameisover = False
found = False
guess = random.randint(1,100)
while not gameisover:
    print(f"You have {tries} attemtps to guess the number")
    user_guess = int(input("Give your guess: "))
    if user_guess == guess:
        gameisover = True
        print(f"You got it! The number was {guess}")
    else:
        tries -= 1
        if user_guess > guess:
            print("Too high.")
        elif user_guess < guess:
            print("Too low.")
        if tries == 0:
            print("You 've run out of attempts.")
            gameisover = True
        else:
            print("Try again.")
        

