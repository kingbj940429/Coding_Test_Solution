''' 1343번 폴리오미노 '''
import sys
input = sys.stdin.readline

graph = input().rstrip()

result = []
flag = True
#.를 기준으로 자른다
strings = graph.split(".")

for i in strings:
    if len(i) <= 0 :
        result.append('.')
        continue
    #홀수면 무조건 -1이다
    if len(i) % 2 != 0 :
        print(-1)
        flag = False
        break
    else:
        for idx, j in enumerate(i):
            if (len(i) - idx <= 2 ) and len(i)%4 != 0:
                result.append('B')
            else:
                result.append('A')
        result.append('.')
if flag == True:
    result = result[:-1]
    print("".join(result))
