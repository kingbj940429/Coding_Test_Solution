'''
최대 길이는 10
각 길이별 가격이 주어짐
'''

# 각 길이별 가격 (0부터 시작)
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

n = int(input())

d = [0] * (n+1)

for i in range(1,n+1):
    temp = 0
    for j in range(i+1):
        temp = max(temp,d[i-j] + p[j])
    d[i] = temp
print(d[n]) 



