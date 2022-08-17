import random
import art
import game_data
print(art.logo)
print(len(game_data.data))
#This must be on dev branch
def giverandom(num):
  x = random.randint(0,49)
  if num == -1: #check if there is a number to achieve inequality
    return x
  else:
    while x == num:
      x=random.randint(0,49)
      print("pesame ston idio")
    return x
def dotheprint(a,b):
  print(f"Compare A: {game_data.data[a]['name']},  {game_data.data[a]['description']}")
  print(art.vs)
  print(f"Compare B: {game_data.data[b]['name']},  {game_data.data[b]['description']}")

def checkanswer(a,b,ans):
    if (a>b and ans == 'A') or (a <b and ans == 'B'):
        return True
    else:
        return False


a = giverandom(-1)
b = giverandom(a)
score = 0
gameover = False
while not gameover:
  dotheprint(a,b)
  ans = input("Who has more followers? Type 'A' or 'B': ") 
  fa = game_data.data[a]['follower_count']
  fb = game_data.data[b]['follower_count']
  if checkanswer(fa,fb,ans):
      score += 1
      print(f"You are right, current score: {score}")
      a = b
      b = giverandom(a)
      
  else:
      gameover = True
      
print(f"Game over! Your score is {score}")
  
   
      