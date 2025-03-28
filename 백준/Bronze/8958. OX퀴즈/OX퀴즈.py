a = int(input())

for n in range(a):
    ox_list = input()
    total_score = 0
    ox_score = 0
    
    for ox in ox_list:
        if ox == 'O':
            ox_score += 1
            total_score = total_score + ox_score
        else:
            ox_score = 0
    
    print(total_score)