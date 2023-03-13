import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    NumberOfRecords = int(sys.stdin.readline().strip())
    for i in range(NumberOfRecords):
        domain, size = sys.stdin.readline().strip().split(" ")
        size = int(size)
        if size > 1000 and ".lmco.com" not in domain:
            print(domain, size)