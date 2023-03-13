import sys

NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    phrase = sys.stdin.readline().strip()
    for letter in phrase:
        if letter.lower() in vowels:
            count += 1
    print(count)