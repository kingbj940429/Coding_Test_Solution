''' 9655번 돌 게임 '''


N = int(input())

d = [0] * 1001

d[0] = 0

for i in range(1,N + 1):
    temp = 1001
    
    for j in range(i+1):
        temp = min(temp, d[i-j-1] + 1)
        if i > 3:
            temp = min(temp, d[i-j-3] + 1)
    d[i] = temp

print(d[N])