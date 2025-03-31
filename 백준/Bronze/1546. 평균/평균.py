a = int(input())
score = list(map(int,input().split()))
M = max(score)
avg = 0

for i in range(a):
    avg += (score[i]/M*100)
    
print(avg/a)