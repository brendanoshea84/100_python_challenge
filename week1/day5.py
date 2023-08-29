# # for loops

# fruits = ["Apples", "Oranges", "Pear"]

# for fruit in fruits:
#     print(fruit)


# exercise
# student_heights = input("Input a list of student heights").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# a = 0
# for t in student_heights:
#     a += t

# average = a / len(student_heights)
# print(average)


# student_scores = [78, 65, 89, 55, 91, 64, 89]
# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

# print(highest_score)
# print(max(student_scores))

# for number in range(4, 10):
#     print(number)


# for number in range(4, 10, 2):
#     print(number)

# random password
import random
import string


number_of_letters = int(input("how many letters"))
number_of_numbers = int(input("number of numbers"))

letters = random.sample(string.ascii_letters, number_of_letters)
numbers = random.sample(range(0, 10), number_of_numbers)

new_password = letters + numbers
new_password = random.sample(new_password, len(new_password))

print(new_password)
