n = int(input())
for i in range(n):
    N = int(input())
    a, b = 1, 0 # 0과 1이 호출된 횟수
    for i in range(N):
        a,b = b, a+b 
    print(a,b)