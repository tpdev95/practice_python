"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

from ex_1 import validate_number

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    validate_number(number, check_zero=False)
    if number % 4 == 0:
        print("Even and multiple of 4")
    elif number % 2 == 0:
        print("Its Even")
    else:
        print("Its Odd")

    num = int(input("A= "))
    check = int(input("B= "))

    while check == 0:
        print("Cant be 0")
        check = int(input("Enter the value of B again = "))
    if num % check == 0:
        print("They are Evenly")
    else:
        print("They are Oddly")
