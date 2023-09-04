# importing random to use randint() function
import random 

# Create a list that the computer can choose from.
list1 = ["Rock", "Paper", "Scissor"] 

# taking users' input
choice = input("Enter Rock, Paper or Scissor: ") 

 # Generating a random element from the list
choice2 = list1[random.randint(0,2)]

# Displaying the random choice of computer
print("Computer choice = ", choice2)

if choice==list1[0]:  # checking if users input is Rock
  if choice2==list1[0]:  # checking if computer choice is also Rock
    print("Draw")
  elif choice2==list1[1]:  # checking if computer choice is Paper
    print("You Loose")
  else:  # user won because computer chose Scissors
    print("You Won")
elif choice==list1[1]:  # checking if users input is Paper
  if choice2==list1[0]:  # checking if computer choice is Rock
    print("You Won")
  elif choice2==list1[1]:  # checking if computer choice is also Paper
    print("Draw")
  else: # user lost because computer chose Scissors
    print("You Loose")
elif choice==list1[2]:  # checking if users input is Scissors
  if choice2==list1[0]:  # checking if computer choice is Rock
    print("You Loose")
  elif choice2==list1[1]:  # checking if computer choice is Paper
    print("You Won")
  else:  # its a draw because computer also chose Scissors
    print("You Draw")
else:
  print("Wrong input")  # in case of user enters undesired input
