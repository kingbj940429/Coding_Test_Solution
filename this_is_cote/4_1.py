''' 4-1 상하좌우 '''

N = int(input())
datas = list(input().split())

pos = [1,1]

for data in datas:
    if(data == 'L'):
        pos[1] -= 1
        if(pos[1] < 1 or pos[1] > N):
            pos[1] += 1
    elif(data == 'R'):
        pos[1] += 1
        if(pos[1] < 1 or pos[1] > N):
            pos[1] -= 1
    elif(data == 'U'):
        pos[0] -= 1
        if(pos[0] < 1 or pos[0] > N):
            pos[0] += 1
    elif(data == 'D'):
        pos[0] += 1
        if(pos[0] < 1 or pos[0] > N):
            pos[0] -= 1
print(pos[0], pos[1])
