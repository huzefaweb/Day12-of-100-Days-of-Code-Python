# number gusseing
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
think_number=random.randint(1, 100)
level=input("Choose a difficulty level 'easy' or 'hard': ")
def number_matching(guess):
  if guess>think_number:
    print("Too High")
  elif guess<think_number:
    print("Too Low")
  elif guess==think_number:
    print(f"You got it the answer is {think_number}")
    return think_number

if level=="easy":
  for i in reversed(range(11)):
    print(f"You have {i} attempts to guess the number.")
    guess=int(input("Make a guess: "))
    matched=number_matching(guess)
    print("Guess Again")
    if guess==matched or i==1:
      break
else:
  for i in reversed(range(5)):
    print(f"You have {i} attempts to guess the number.")
    guess=int(input("Make a guess: "))
    matched=number_matching(guess) 
    if guess==matched:
      break
    elif i==1:
      print("You run out of guesses 'You Lose'")
      break 
    print("Guess Again")
