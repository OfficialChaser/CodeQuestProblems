import sys
import string

NumberOfCases = int(sys.stdin.readline().strip())

letters = string.ascii_letters

for _ in range(NumberOfCases):
    check = False
    resletters = []
    grtletters = []
    greeting, response = sys.stdin.readline().strip().split("|")
    for char in response:
        if char not in resletters and char in letters:
            resletters.append(char.lower())
    for char in greeting:
        if char not in grtletters and char in letters:
            grtletters.append(char.lower())
    for char in resletters:
        if char not in grtletters:
            print("You're not a secret agent!")
            check = True
            break
    if check == False:
        print("That's my secret contact!")
        

    

