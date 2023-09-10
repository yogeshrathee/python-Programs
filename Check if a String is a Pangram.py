import string

sentence = input("Enter a sentence: ").lower()
is_pangram = all(letter in sentence for letter in string.ascii_lowercase)

if is_pangram:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
