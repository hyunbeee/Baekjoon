n = int(input())
a = set(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

for x in nums:
    if x in a:
        print(1)
    else:
        print(0)