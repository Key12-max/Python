# it requires the function to return boolean values and then
# passes each element in the iterable through the function.
#filter(func, iterable)

#some examples
#the ff list(iterable) of the scores of 10 students in a Math exam.
# Let's filter out those who passed with scores more than 75 using filter
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)
