import random
list1 = ["Rock", "Paper", "Scissor"]
choice = input("Enter Rock, Paper or Scissor: ")
choice2 = list1[random.randint(0,2)]
print("Computer choice = ", choice2)
if choice==list1[0]:
  if choice2==list1[0]:
    print("Draw")
  elif choice2==list1[1]:
    print("You Loose")
  else:
    print("You Won")
elif choice==list1[1]:
  if choice2==list1[0]:
    print("You Won")
  elif choice2==list1[1]:
    print("Draw")
  else:
    print("You Loose")
elif choice==list1[2]:
  if choice2==list1[0]:
    print("You Loose")
  elif choice2==list1[1]:
    print("You Won")
  else:
    print("You Draw")
else:
  print("Wrong input")
