list1 = [int(input("Enter a number for list 1: ")) for _ in range(5)]
list2 = [int(input("Enter a number for list 2: ")) for _ in range(5)]
intersection = list(set(list1) & set(list2))
print(f"The intersection of the lists is: {intersection}")
