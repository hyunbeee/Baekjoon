n = int(input())

for i in range(n):
    stack = []
    m = input()
    
    for j in m:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 리스트에 괄호가 없을 경우
                print('NO')
                break
    else: # break문에 걸리지 않고 for문이 끝났을 경우
        if not stack: 
            print('YES')
        else: 
            print('NO')