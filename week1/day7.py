import random
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
blank_space = []
game_on = True
for b in word:
    blank_space.append("_")


def guessing_a_letter():

    guess = input("guess a letter?")
    position = 0
    lives = 0

    for l in word:
        print(f"position: {position}")
        if l == guess:
            blank_space[position] = guess
            print("correct")

        else:
            lives += 1
            print("wrong")
        position += 1
    print(blank_space)

    if ("_" not in blank_space):
        print("line 29")
        game_on = False

    while game_on == True:
        guessing_a_letter()

    else:
        print("You won!")


guessing_a_letter()
