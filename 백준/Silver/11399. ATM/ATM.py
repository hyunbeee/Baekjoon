n = int(input())

num = list(map(int, input().split()))
num.sort()
result = 0
time = 0
for i in range(n):
    time += num[i]
    result += time
print(result)