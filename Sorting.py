import sys
NumberOfCases = int(sys.stdin.readline().strip())

for i in range(NumberOfCases):
    nums = [int(i) for i in sys.stdin.readline().strip().split(",") if i != ","]
    nums.sort()
    for i in nums[:-1]:
            print(f'{i},', end='')
    print(nums[-1])