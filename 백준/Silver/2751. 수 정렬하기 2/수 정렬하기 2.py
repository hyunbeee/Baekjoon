import sys

n = int(input())
num = []

for i in range(n):
    m = int(sys.stdin.readline())
    num.append(m)
    
num.sort()

for j in num:
    print(j)