# create a greeting function
# def greet():
#     name1 = input("What is your name?")
#     last1 = input("what is your last name?")
#     print(f"Good morning {name1} {last1}")


# greet()


# Function that allows input
# def greet_with_name(name2):
#     print(f"good morning {name2}")


# greet_with_name("brendan")


# Function that allows 2 input
# def greet_with_name(name, location):
#     print(f"good morning {name}")
#     print(f"hows {location} weather today?")


# greet_with_name("brendan", "Brisbane")

# function with keywords
# import math


# def greet_with_name(name, location):
#     print(f"good morning {name}")
#     print(f"hows {location} weather today?")


# greet_with_name(location="Brisbane", name="Brendan")

# # Painting a wall


# def paint_calc(height, width, cover):
#     total = (height*width)/cover
#     total = math.ceil(total)
#     print(f"You'll need {total} cans of paint.")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# # testing prime numbers
# def prime_checker(number):
#     is_prime = True
#     for n in range(2, number):
#         if (number % n == 0):
#             is_prime = False
#     if (is_prime == True):
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# n = int(input("Check this number: "))
# prime_checker(number=n)


# Cipher exercise

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "y", "z",]

direction = input("type encode or decode\n")
text = input("type your message\n").lower()
shift = int(input("type the shift number\n"))


def encrypt(plain_text, shift_amount, new_direction):
    cipher_text = ""
    if new_direction == "decode":
        shift_amount *= -1

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encode is {cipher_text}")


encrypt(plain_text=text, shift_amount=shift, new_direction=direction)
