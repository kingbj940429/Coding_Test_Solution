''' 2865번 나는 위대한 슈퍼스타K '''
n, m, k = map(int, input().split())
participants = [0.0] * n

for i in range(m):
    line = input().split()
    
    for j in range(n):
        participant, skill = int(line[2*j])-1, float(line[2*j+1])
        participants[participant] = max(participants[participant], skill)

print(round(sum(sorted(participants, reverse=True)[:k]),1))


        

        
        
    

