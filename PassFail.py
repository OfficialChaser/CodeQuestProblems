import sys

cases = int(sys.stdin.readline().strip())

for i in range(cases):
    grade = int(sys.stdin.readline().strip())
    if grade >= 70:
        print("PASS")
    else:
        print("FAIL")