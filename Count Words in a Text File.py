file_name = input("Enter the name of the text file: ")

try:
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"The number of words in the file is: {word_count}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
