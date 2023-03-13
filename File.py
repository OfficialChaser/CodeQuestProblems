import sys
NumberOfCases = int(sys.stdin.readline().strip())

filetypes = []
for i in range(NumberOfCases):
    *_, type = sys.stdin.readline().strip().split(".")
    filetypes.append(type)


dupcheck = []
final = []
for file in filetypes:
    if file not in dupcheck:
        dupcheck.append(file)
        num = filetypes.count(file)
        final.append([file, num])
    
for set in final:
    print(set[0], set[1])
