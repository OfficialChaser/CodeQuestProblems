import sys

cases = int(sys.stdin.readline().strip())

for i in range(cases):
    speed, birthdayCheck = sys.stdin.readline().strip().split(" ")
    speed = int(speed)
    increased = 0
    if birthdayCheck == "false":
        birthdayCheck = False
    elif birthdayCheck == "true":
        birthdayCheck = True
        increased = 5 
    if speed <= 60 + increased:
        print("no ticket")
    elif speed >= 61 + increased and speed <= 80 + increased:
        print("small ticket")
    else:
        print("big ticket")