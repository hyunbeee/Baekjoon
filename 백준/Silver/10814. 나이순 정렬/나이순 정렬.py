n = int(input())
mem = []

for i in range(n):
    age, name = input().split()
    mem.append((int(age), name))

mem.sort(key=lambda x: x[0])
 
for age, name in mem:    
    print(age, name)