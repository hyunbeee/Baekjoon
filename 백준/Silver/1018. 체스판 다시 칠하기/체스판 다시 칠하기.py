n,m = map(int, input().split())

board = []
result = []

for i in range(n):
    board.append(input())

for j in range(n-7):
    for k in range(m-7):
        black = 0
        white = 0
    
        for a in range(j, j+8):
            for b in range(k, k+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        black += 1
                    if board[a][b] != 'W':
                        white += 1
                else:
                    if board[a][b] != 'W':
                        black += 1
                    if board[a][b] != 'B':
                        white += 1
        result.append(black)
        result.append(white)
print(min(result))