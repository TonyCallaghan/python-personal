# For all the numbers between 1 and 100(including 100), create a variable called answer,
#which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)

answer =  [x for x in range(1,101) if x % 12 == 0]
