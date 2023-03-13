import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    nums = sys.stdin.readline().strip().split(" ")
    nums = [(int(i)) for i in nums]
    sum = nums[0] + nums[1]
    product = nums[0] * nums[1]
    print(f"{sum} {product}")