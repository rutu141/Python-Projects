#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random


# Allow the player to submit a guess for a number between 1 and 100.
actual_number=random.randint(1,101)
print(actual_number)
# guess=int(input("Guess a number between 1-100 :"))
level=input("Select the level of the game (Hard/Easy)")
if level=="Hard":
  turns=5
else:
  turns=10


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def compare(turns):
  if guess>actual_number:
    print("Too High")
    return turns-1
  elif guess<actual_number:
    print("Too Low")
    return turns-1
  else:
    print("Congratulations you Win !!!!")
    return 100

while(turns>0):
  #actual_number=random.randint(1,101)
  #print(actual_number)
  guess=int(input("Guess a number between 1-100 :"))
  turns=compare(turns)
  if turns==100:
    print("Well Played!!")
    break
  else:
    print(f"You have {turns} left")
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

