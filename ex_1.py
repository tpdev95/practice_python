"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""
def validate_name(name):
    try:
        int(name)
        return False
    except:
        return len(name) > 0


def validate_number(number, check_zero=True):
    try:
        number = int(number)

        #EL SEGUNDO ARGUMENTO(CHECK ZERO) FUNCIONA COMO INTERRUPTOR PARA HACER O NO LAS 2 LINEAS DE ABAJO) OPCIONAL YA TIENE TRUE SETEADO COMO DEFAULT
        if check_zero:
            return number > 0
        return True
    except:
        return False


if __name__ == "__main__":

    name = input("Enter your name: ")

    while validate_name(name) == False:
        print("Wrong name")
        name = input("Enter your name: ")

    age = input("Enter your age: ")

    while validate_number(age)== False:
        print("wrong age")
        age = input("enter your age again: ")

    year = 100 - int(age) + 2019

    if int(age) >= 100:
        print("Hi "+name+" you were 100 years old in "+str(year))
    else:
        print("Hi "+name+" in "+str(year)+"  you will be 100 years old")

#
# def yearcalculator(age):
#     name = input("Enter your name: ")
#     age = input("Enter you age: ")
#     if name != type("asd") and age != type(23):
#         print("You cant enter numbers as your name or a word as your age")
#         name = input("Enter your name again: ")
#         age = input("Enter you age again: ")
#     else:
#
#
# yearcalculator(age)
