
list = ["ipad", "cookie"]
total = []
from replit import clear
import random
import hangmanart

print(hangmanart.logo)

randword = random.choice(list)
hangman = 5
location = -1
letters = 0
wordentered = []

for a in randword:
  letters += 1
  total.append("_")
  

print("".join(total))

while hangman > 0 and "".join(total) != randword:
  i = input("\nTake a Guess!\n")
  clear()
  if i in wordentered:
    print("".join(total))
    print("You've already tried that word")
  else:
    wordentered.append(i)
    if i in randword:
      for b in randword:
        location += 1
        if b == i:
          total[location] = b
          print(hangmanart.stages[hangman])
          print("is in the word!")
          print("".join(total))
      location = location - location - 1
    else:
      hangman -=1
      print(hangmanart.stages[hangman])
      print("".join(total))
      print("is not in the word!")

if hangman < 1:
  print("LOSER YOU LOST")
else:
  print("Winna winna chicken dinna")