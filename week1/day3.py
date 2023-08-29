print("Welcome to the rollercoaster")
height = int(input("What is your height in CM?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Whats is your age?"))

    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("your ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")

    wants_photo = input("Do you want a photo taken? Y or N")
    if wants_photo == "Y":
        bill += 3

    print(f"You final bill is ${bill}")
else:
    print("Sorry, you have to be taller to ride the rollercoaster")


# Pizza exerise
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total = 0

if size == "S":
    total = 15
    if add_pepperoni == "Y":
        total += 2
elif size == "M":
    total = 20
    if add_pepperoni == "Y":
        total += 3
else:
    total = 25
    if add_pepperoni == "Y":
        total += 3
if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}.")
