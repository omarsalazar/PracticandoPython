message = input("Type word: ")

print("Capital Letters: ", sum(1 for c in message if c.islower()))
