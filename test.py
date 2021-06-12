import random

name = input("Input Name?\n")

def run():

  print(f"Hello, {name}, let's play!")
  print("Go!")

  with open("words.txt") as f:
    Game = f.read().split()
    
  word = random.choice(Game)

  guesses = " "

  turns = 8

  while turns > 0:

    failed = 0

    for char in word:

      if char in guesses:
        print(char)

      else:

        print("_")

        failed += 1

    if failed == 0:
      print("Winner!")
      choice = input("Play Again? y/n\n")
      if "y" in choice:
        run()
      elif "n" in choice:
        sys.exit()

      else:

        print("Something went wrong, type y or n.")

    guess = input("Guess Letters:")

    guesses += guess

    if guess not in word:

      turns -= 1

      print("Wrong!")
      print(f"You have {turns} more guesses.")

      if turns == 0:
        print("Loser!")
        choice = input("Play Again? y/n\n")
        if "y" in choice:
          run()
        elif "n" in choice:
          sys.exit()
          
        else:

          print("Something went wrong, type y or n.")
run()