
# Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, 
# which is a new list that is the intersection of the two. Your output should be [3,4] . 

# Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, 
# which is a new list with each word reversed and in lower case. Your output should be ['eile', 'mit', 'ttam'] 

answer = [num for num in range(1,5) if num in range(3,7)]

answer2 = [person[::-1].lower() for person in ["Elie","Tim", "Matt"]]

