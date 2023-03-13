import sys
import math

NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    height = float(sys.stdin.readline().strip())
    radius = (40075 / math.pi) / 2
    new_radius = radius + height 
    answer = (new_radius * 2) * math.pi
    answer = round(answer, 1)
    print(answer)