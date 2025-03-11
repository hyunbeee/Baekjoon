n = int(input())
m = map(int, input().split())
r = int(input())
count = 0

for i in m:
    if i == r:
        count += 1

print(count)