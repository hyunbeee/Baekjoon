a = int(input())

for _ in range(a):
    n, word = input().split()
    for i in word:
        print(i*int(n), end='')
    print()