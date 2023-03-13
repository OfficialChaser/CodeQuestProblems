import sys

NumberOfCases = int(sys.stdin.readline().strip())


for i in range(NumberOfCases):
    check = False
    small, large, total = sys.stdin.readline().split(" ")
    small = int(small)
    large = int(large)
    total = int(total)
    totlarge = large * 5
    if small + totlarge < total:
        print('false')
    elif small + totlarge == total:
        print('true')
    else:
        for i in range(small + 1):
            if i == total:
                 check = True
                 break
        if check == True:
            print('true')
        else:
            for i in range(0, totlarge + 1, 5):
                if i == total:
                    check = True
            if check == True:   
                print('true')
            else:
                combinations = []
                for num in range(small + 1):
                    for num2 in range(0, totlarge + 1, 5):
                        added = num + num2
                        combinations.append(added)
                if total in combinations:
                    print('true')
                else:
                    print('false')


        