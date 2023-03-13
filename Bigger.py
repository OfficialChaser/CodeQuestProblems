import sys

cases = int(sys.stdin.readline().strip())

for i in range(cases):
    nums = [int(i) for i in sys.stdin.readline().strip().split(" ") if i != " "]
    nums.sort(reverse=True)
    print(nums[0])