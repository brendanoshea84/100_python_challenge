import random
# papper siccor rock game

computer_choice = ["p", "s", "r"]
player1 = input("Paper, siccor and rock (p, s, r)")

computer = random.choice(computer_choice)
you_win = "You won!"
comp_win = "Computer Won!"

if computer == player1:
    print("A draw!")
elif player1 == "p":
    if computer == "s":
        print(comp_win + " :"+computer)
    else:
        print(you_win + " :"+computer)
elif player1 == "s":
    if computer == "p":
        print(you_win + " :"+computer)
    else:
        print(comp_win + " :"+computer)
else:
    if computer == "p":
        print(you_win + " :"+computer)
    else:
        print(comp_win + " :"+computer)


# random bill payer
# Import the random module here
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

get_number_of_names = len(names) + 1
random_num = random.randrange(0, get_number_of_names)

random_name = names[random_num]
print(f"{random_name} is going to buy the meal today!")


# Chnage maps

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0])
vertical = int(position[0])

map[vertical - 1][horizonal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
