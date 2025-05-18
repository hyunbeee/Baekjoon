from collections import deque

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    a = deque(list(map(int, input().split())))
    cnt = 1
    while 1:
        if m == 0:
            if a[0] == max(a):
                print(cnt)
                break
            else:
                a.append(a[0])
                a.popleft()
                m = n-1
        else:
            if a[0] == max(a):
                cnt += 1
                a.popleft()
                n -= 1
                m -= 1
            else:
                a.append(a[0])
                a.popleft()
                m -= 1