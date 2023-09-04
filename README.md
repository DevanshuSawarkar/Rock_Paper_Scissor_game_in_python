 ## Rock, Paper, Scissors Game in Python

### Step 1: Import the necessary libraries

```
import random
```

### Step 2: Create a list of possible choices

```
list1 = ["Rock", "Paper", "Scissor"]
```

### Step 3: Get the user's choice

```
choice = input("Enter Rock, Paper or Scissor: ")
```

### Step 4: Generate a random choice for the computer

```
choice2 = list1[random.randint(0,2)]
```

### Step 5: Display the computer's choice

```
print("Computer choice = ", choice2)
```

### Step 6: Determine the winner

```
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
  else:  # It is a draw because the computer also chose Scissors
    print("You Draw")
else:
  print("Wrong input")  # in case of user enters undesired input
```

### Step 7: Run the game

```
if __name__ == "__main__":
    main()
```
