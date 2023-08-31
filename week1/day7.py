import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
blank_space = []
lives = 0
for b in word:
    blank_space.append("_")


def guessing_a_letter():
    global lives
    game_on = True
    guess = input("guess a letter?")
    position = 0

    print(f"lives line 15 : {lives}")
    correct_letter = 0

    for l in word:
        print(f"position: {position}")
        if l == guess:
            correct_letter += 1
            blank_space[position] = guess
            print("correct")
        else:
            print("wrong")
        position += 1
    print(blank_space)

    if correct_letter == 0:
        lives += 1
    else:
        correct_letter = 0

    print(f"lives: {lives}")
    if ("_" not in blank_space):
        print("line 29")
        game_on = False

    if lives == 7:
        game_on = False

    while game_on == True:
        guessing_a_letter()

    else:
        if lives == 7:
            print("You died")
        else:
            print("You won!")


guessing_a_letter()
