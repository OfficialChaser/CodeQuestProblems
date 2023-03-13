import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    nums = sys.stdin.readline().strip().split(":")
    nums = [(float(i)) for i in nums]
    v = nums[0]
    x = nums[1]
    z = v * 5
    if v >= x:
        print("SWERVE")
    elif z >= x:
        print("BRAKE")
    else:
        print("SAFE")
