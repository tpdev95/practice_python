from asd1 import validate_number

if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    c = []
    for i in a:
        if i < 5:
            b.append(i)
        else:
            pass

    print(b)



    num = input("Enter a number: ")
    validate_number(num, True)
    while validate_number(num, True) == False:
        num = input("enter a number again: ")
    else:
        for i in a:
            if i < int(num):
                c.append(i)

    print(c)
