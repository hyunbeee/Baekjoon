word = input().strip()

alph = "abcdefghijklmnopqrstuvwxyz"

for i in alph:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')