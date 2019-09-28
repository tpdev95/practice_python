from asd1 import validate_number

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
