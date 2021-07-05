# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, 
# which is a new list containing the first letter of each name in the list. 

# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  

answer = [person[0] for person in ["Ellie", "Tim", "Matt"]]

answer2 = [num for num in range(1,7) if num % 2 == 0]
