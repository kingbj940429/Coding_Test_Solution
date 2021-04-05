''' 그리디 알고리즘 : 1이 될때까지 '''
N, K = map(int, input().split())
cnt = 0
while N > 1:
    if(N%K == 0):
        N = N//K
    else:
        N -= 1
    cnt += 1
print(cnt)



