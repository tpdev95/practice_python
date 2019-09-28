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
