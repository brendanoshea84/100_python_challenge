# Function with Outputs

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't write anything..."

#     f_name = f_name.capitalize()
#     l_name = l_name.capitalize()

#     return (f_name + " " + l_name)
#     # return stop the function
#     print("this wont work")


# New_name = format_name("brendan", "OSHEAS")
# print(New_name)

# print(format_name(input("What is your first name? "),
#       input("What is your last name? ")))


# # Practise with months and leap years
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     if month > 12 or month > 1:
#         return "enter month by number 1-12"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     else:
#         return month_days[month-1]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# Doc string

"""
Multi line comment letter
doc your functions 
"""

# Calculator function
print("line 60")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1 / n2


def calculator():
    calculator_on = True
    n1 = 0
    while calculator_on:
        if n1 == 0:
            n1 = float(input("What is your first number?"))
            type_of_cal = input("what cal symbol? : + - * /")
            n2 = float(input("What is your second number?"))
        else:
            type_of_cal = input("what cal symbol?")
            n2 = float(input("What is your second number?"))

        if type_of_cal == "+":
            answer = add(n1, n2)
            print(f"total = {answer}")
        elif type_of_cal == "-":
            answer = subtract(n1, n2)
            print(f"total = {answer}")
        elif type_of_cal == "*":
            answer = mult(n1, n2)
            print(f"total = {answer}")
        else:
            answer = div(n1, n2)
            print(f"total = {answer}")

        keep_cal = input("keep cal?: Y or N")

        if keep_cal == "N":
            calculator_on = False
            print("restart")
            calculator()
        else:
            n1 = answer


calculator()
