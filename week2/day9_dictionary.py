programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# retrieving Items from Dictionary
print(programming_dictionary["Bug"])

# adding to the dictionary
programming_dictionary["loop"] = "action of doing something over and over again"
print(programming_dictionary)

# create an empty loop or clearing a diction
empty_dictionary = {}
# programming_dictionary = {}

# change the value from key word
programming_dictionary["Bug"] = "Lets change the bug value"
print(programming_dictionary)

# loops
print("LOOP")

for key in programming_dictionary:
    print(key)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Grading exercie
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for score in student_scores:
    name = score
    grade = student_scores[score]
    if (grade > 90):
        grade = "Outstanding"
    elif (90 >= grade >= 81):
        grade = "Exceeds Expectations"
    elif (80 >= grade >= 71):
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[name] = grade

print(student_grades)
