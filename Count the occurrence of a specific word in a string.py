string_ = "Yogesh is a boy and Yogesh loves to play cricket."
x = input("Enter the word you want to check: ")
main = string_.split(" ")
count = 0
for i in range(len(main)):
    if main[i] == x:
        count += 1
print(count)