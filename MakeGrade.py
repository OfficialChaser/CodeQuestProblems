import sys

cases = int(sys.stdin.readline().strip())

import math

def normal_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals

for i in range(cases):
    students, answers = sys.stdin.readline().strip().split(" ")
    students = int(students)
    question_amt = len(answers)
    for student in range(students):
        name, choices = sys.stdin.readline().strip().split(" ")
        count = 0
        correct = 0
        for choice in choices:
            if choice == answers[count]:
                correct += 1
            count += 1
        percentage = normal_round((correct / question_amt), 3) * 100
        percentage = round(percentage, 3)
        print(f'{name} {percentage}% ', end='')
        if percentage >= 90:
            print("A")
        elif percentage >= 80 and percentage < 90:
            print("B")
        elif percentage >= 70 and percentage < 80:
            print("C")
        elif percentage >= 60 and percentage < 70:
            print("D")
        else:
            print("F")