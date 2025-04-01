n, m = map(int,input().split())
num = list(map(int,input().split()))
M_num = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = num[i]+num[j]+num[k]
            if total <= m:
                M_num = max(M_num, total)
print(M_num)