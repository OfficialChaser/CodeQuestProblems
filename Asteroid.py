import sys
import math

NumberOfCases = int(sys.stdin.readline().strip())

for _ in range(NumberOfCases):
    asteroids = int(sys.stdin.readline().strip())
    coords = []
    for asteroid in range(asteroids):
        x, y = sys.stdin.readline().strip().split(" ")
        x = int(x)
        y = int(y)
        total = math.sqrt((x ** 2) + (y ** 2))
        coords.append([total, x, y])
        coords.sort()
    count = 0
    for _ in coords:
        print(coords[count][1], coords[count][2])
        count += 1
        