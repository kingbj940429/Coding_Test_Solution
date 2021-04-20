''' 2822번 점수 계산 '''

score = []
for i in range(8):
    temp = int(input())
    score.append([i,temp])
score.sort(key=lambda x:x[1], reverse=True)

result = 0
for i in range(5):
    result += score[i][1]
print(result)

result = []
for i in range(5):
    result.append(score[i][0] + 1)
result.sort()
for data in result:
    print(data, end=" ")

    

