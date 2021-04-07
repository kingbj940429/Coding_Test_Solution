''' 12865번 평범한 배낭 '''

from itertools import combinations

# 물품의수, 최대 무게
N, K = map(int,input().split())

#물품들의 무게와 가치
datas = []

#각 물품의 개수마다 최대의 가치값
max_result = []

#입력값
for _ in range(N):
    temp = []
    W,V = map(int, input().split())
    temp.append(W)
    temp.append(V)
    datas.append(temp)

#combination으로 모든 가능성 열어두기(브루트포스)
combi_data = []

result_data = []
for i in range(1,N+1):
    # 물품의 개수 i개를 가지고 가치를 판단한다. 
    combi_data = list(combinations(datas, i))
    max_value_per = []

    for j in range(len(combi_data)):
        value_list = []
        sum_weight = 0
        sum_value = 0
        for k in range(len(combi_data[j])):
            sum_weight += combi_data[j][k][0]
            sum_value += combi_data[j][k][1]
        if(sum_weight > K):
                continue
        else:
            value_list.append(sum_value)
        max_value_per.append(max(value_list))
    result_data.append(max_value_per)

result = sum(result_data,[])
print(max(result))

    
##답
import sys

r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])

        

    





