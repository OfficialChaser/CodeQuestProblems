import sys

cases = int(sys.stdin.readline().strip())

for i in range(cases):
    a, b = sys.stdin.readline().strip().split(" ")
    a = int(a)
    b = int(b)
    if a == b:
        print((a + b) * 2)
    else:
        print((a + b))