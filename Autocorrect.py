import sys

NumberOfCases = int(sys.stdin.readline().strip())

for _ in range(NumberOfCases):
    d, w = sys.stdin.readline().strip().split(" ")
    d = int(d) 
    w = int(w)
    wordslist = []
    for _ in range(d):
        word = sys.stdin.readline().strip()
        wordslist.append(word)
    


