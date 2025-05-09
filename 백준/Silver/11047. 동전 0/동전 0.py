n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

result = 0
for C in coin:
    if k >= C:
        result += k // C
        k = k % C
        if k <= 0:
            break

print(result)