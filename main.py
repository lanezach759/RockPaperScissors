import random, sys

print ("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:     # Main game
  print ("%s wins %s losses %s ties" % (wins, losses, ties))
  while True:   # Player input loop
    print ("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
    pmove = input()
    if pmove == "q":
      sys.exit()
    elif pmove == 'r' or pmove == 'p' or pmove == 's':
      break

  if pmove == 'r':
    print("ROCK versus...")
  elif pmove == 'p':
    print ("PAPER versus...")
  elif pmove == 's':
    print ("SCISSORS versus...")

# Random computer move
  randomnum = random.randint(1, 3)
  if randomnum == 1:
    cmove = 'r'
    print ("ROCK")
  elif randomnum == 2:
    cmove = 'p'
    print ("PAPER")
  elif randomnum == 3:
    cmove = 's'
    print ("SCISSORS")
 
  if pmove == cmove:
    print ("It's a tie!")
    ties += 1
  elif pmove == 'r' and cmove == 'p':
    print ("You lose!")
    losses += 1
  elif pmove == 'p' and cmove == 'r':
    print ("You win!")
    wins += 1
  elif pmove == 'r' and cmove == 's':
    print ("You win!")
    wins += 1
  elif pmove == 's' and cmove == 'p':
    print ("You win!")
    wins += 1
  elif pmove == 's' and cmove == 'r':
    print ("You lose!")
    losses += 1
  elif pmove == 'p' and cmove == 's':
    print ("You lose!")
    losses += 1