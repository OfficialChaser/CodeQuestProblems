import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    decoder = []
    codes = []
    order = sys.stdin.readline().strip()
    [decoder.append(i) for i in order]
    for i in range(NumberOfCases - 1):
        code = [sys.stdin.readline().strip().split(" ")]
        [codes.append(i) for i in code]
    break

number = []
for line in codes:
    for seq in line:
        for num in seq:
            
            if num != "-":
                number.append(num)
                print(decoder[number])
            elif num == " ":
                [print(i, end="") for i in number]
                number.clear()
            else:
                [print(i, end="") for i in number]
                number.clear()
    


    