''' 1476번 날짜 계산 '''

# 지구, 태양, 달의 수
E, S, M = map(int, input().split())
#print(lcms([E, S, M]))
earth , sun, moon = 1,1,1
result = 0
while True:
    result += 1
    if earth == E and sun == S and moon == M :
        break
    
    earth %= 15
    earth += 1
    sun %= 28
    sun += 1
    moon %= 19
    moon += 1

print(result)


