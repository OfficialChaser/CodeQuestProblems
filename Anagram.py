import sys

NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    word1, word2 = sys.stdin.readline().strip().split("|")
    if word1 == word2:
        print(f'{word1}|{word2} = NOT AN ANAGRAM')
    else:
        list1 = []
        list2 = []
        for char in word1:
            list1.append(char)
        for char in word2:
            list2.append(char)
        list1.sort()
        list2.sort()
        if list1 == list2:
            print(f'{word1}|{word2} = ANAGRAM')
        else:
            print(f'{word1}|{word2} = NOT AN ANAGRAM')

