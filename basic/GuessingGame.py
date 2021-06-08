from random import randint

number = randint(1,20)
print("I'm thinking of a number betwwen 1 and 20:")
for guessesTaken in range(0,5): # 5 chances to guess
    print("Take a guess.")
    guess = int(input())
  
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        break # ends for loop
    
if guess == number:
    print("Correct")
else:
    print("Incorrect")
print("The number i was thinking of was " + str(number))
  
