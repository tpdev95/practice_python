"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""
from asd1 import validate_number

if __name__=="__main__":
    a = []

    num = input("enter a number: ")
    validate_number(num, True)
    while validate_number(num, True) == False:
        num = input("Only numbers and cant be 0: ")
    else:
        for i in range(2, 11):
            if i % int(num) == 0:
                a.append(i)

    print(a)
