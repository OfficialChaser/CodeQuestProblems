import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    num = int(sys.stdin.readline().strip())
    if num < 0:
        print('NEGATIVE')
    else:
        print("POSITIVE")