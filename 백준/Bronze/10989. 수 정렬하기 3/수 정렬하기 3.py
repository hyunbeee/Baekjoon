import sys

input = sys.stdin.readline

n = int(input())

# 10001 크기 리스트
count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1
    
for j in range(10001):
    if count[j] != 0: # count[j]이 1이상이라면
        for k in range(count[j]): # 그 값만큼 출력
            print(j)