''' 18248번 제야의 종 '''

N, M = map(int,input().split())

graph = [0] * (N+1)

for i in range(1,N+1):
    graph[i] = list(map(int,input().split()))

is_possible = True
is_1 = True
is_0 = True
cnt = 0

for i in range(1, 1+N):
    for j in range(M):
        if graph[j][i] == 1 and is_1 == True :
            cnt +=1
            is_1 = False
        elif graph[j][i] == 0 and is_0 == True :
            cnt +=1
            is_0 = False
        if cnt >= 2:
           is_possible = False

if is_possible == True:
    print("YES") 
else:
    print("NO")

    


