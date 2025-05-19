N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_count = {}
for n in N_list:
    try:
        N_count[n] += 1
    except:
        N_count[n] = 1

result = []
for m in M_list:
    try: 
        result.append((N_count[m]))
    except:
        result.append(0)

for i in result:
    print(i, end = ' ')