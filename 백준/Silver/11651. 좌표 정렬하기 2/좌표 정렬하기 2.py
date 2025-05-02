n=int(input())
num=[]
for i in range(n):
    a, b = map(int, input().split())
    num.append([b, a])
nums = sorted(num)
for b,a in nums:
    print(a, b)