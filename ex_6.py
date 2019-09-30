"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""
a = input("enter a word: ")

def reverse_slicing(w):
    return w[::-1]

b = reverse_slicing(a)

if a == b:
    print("Palindrome")
else:
    print("!Palindrome")
