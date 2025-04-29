n = int(input())
num = []

for i in range(n):
    m = int(input())
    if m == 0:
        num.pop()
    else:
        num.append(m)
print(sum(num))