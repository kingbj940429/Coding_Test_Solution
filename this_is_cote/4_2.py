''' 4-2 시각 '''
'''
접근
1) 시간에 만약 3이 있으면 break 걸고 cnt 증가
2) 분과 초는 0~59 까지임
'''

N = int(input())

cnt = 0
for i in range(N+1):
    if(i%10 == 3):
        cnt += 60*60
    else:
        for j in range(60):
            if('3' in str(j)):
                cnt += 60
            else:
                for k in range(60):
                    if('3' in str(k)):
                        cnt += 1
print(cnt)

