a = int(input())
num = list(map(int,input().split()))
sosu = 0

for i in num:
    if i>1:
        for x in range(2, i+1):
            if i%x == 0:
                if i == x:
                    sosu += 1
                break
                
print(sosu)