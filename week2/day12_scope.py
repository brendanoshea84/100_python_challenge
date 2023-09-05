# # Scope
# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside the function: {enemies}")


# increase_enemies()
# print(f"enemies outside the function: {enemies}")

# # Local scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()
# # print(potion_strength)

# # global scope
# player_heath = 10


# def drink_potion():
#     potion_strength = 2
#     print(player_heath)


# drink_potion()  # 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print("line: 39")
#         print(player_heath)
#     drink_potion()


# game()


# game_level = 3


# def create_enemy():
#     enemies = ["Skelton", "Zombie", "Aliens"]

#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)


# create_enemy()

# Modifying Global scope

# enemies = 1


# def increase_enemies():

#     print(f"enemies inside the function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside the function: {enemies}")

# Exercise
import random


def guessing_number():
    game_on = True
    rand_number = random.randint(1, 100)
    players_guesses = 0
    number_of_guesses = 0
    print("Welcome to the random game, 1-100 ")
    diff = input("Easy of Hard? E or H ")

    if diff == "E":
        number_of_guesses = 10
    elif diff == "H":
        number_of_guesses = 5
    else:
        guessing_number()

    while game_on:
        if number_of_guesses == players_guesses:
            print(f"Out of guesses, the number was {rand_number}")
            game_on = False

        print(f"{players_guesses} out of {number_of_guesses}")
        guess = int(input("What number do you guess?"))

        if guess > rand_number:
            print("Too High!")
            players_guesses += 1
        elif rand_number > guess:
            print("to low")
            players_guesses += 1
        else:
            print(f"Correct! The number was {rand_number}")
            game_on = False

    else:
        play_again = input("Do you want to play again? y or n")
        if play_again == "y":
            guessing_number()
        else:
            print("GOOD BYE")


guessing_number()
