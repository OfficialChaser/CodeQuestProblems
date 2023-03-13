import sys

NumberOfCases = int(sys.stdin.readline().strip())

vowels = ["a", "e", "i", "o", "u"]

for i in range(NumberOfCases):
    txt = [i for i in sys.stdin.readline().strip()]
    print(txt)
    count = 0
    for letter in txt:
        if letter in vowels:
            print(txt[count + 1], end="")
            count += 2
        else:
            count += 1
    print()