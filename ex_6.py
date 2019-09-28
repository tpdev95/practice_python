a = input("enter a word: ")

def reverse_slicing(w):
    return w[::-1]

b = reverse_slicing(a)

if a == b:
    print("Palindrome")
else:
    print("no palindromo gato")
