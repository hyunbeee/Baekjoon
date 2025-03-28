a = int(input())  

for i in range(a):
    H, W, N = map(int, input().split())  
    
    H_num = (N % H)  
    W_num = (N // H)

    if H_num == 0:
        H_num = H
    else:
        W_num += 1 
        
    print(f"{H_num}{W_num:02d}")
