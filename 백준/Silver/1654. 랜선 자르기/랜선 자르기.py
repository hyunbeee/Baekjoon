k, n = map(int, input().split())
lan = []

for i in range(k):
    r = int(input())
    lan.append(r)

start = 1
end = max(lan)
result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in lan:
        cnt += (i // mid)

    if cnt >= n:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)