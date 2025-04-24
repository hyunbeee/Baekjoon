n, m = map(int, input().split())

for i in range(n, m+1):
    if i == 1: # 1은 통과
        continue
    for j in range(2, int(i**0.5)+1): # 2부터 i의 제곱근까지 나누어 떨어지는지 확인
        if i % j == 0: # 나누어 떨어진다면 소수가 아니기 때문에 종료 ( else문 실행 X )
            break
    else:
        print(i) # 소수 출력