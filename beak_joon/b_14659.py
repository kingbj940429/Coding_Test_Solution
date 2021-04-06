''' 14659번 한조서열정리하고옴ㅋㅋ '''
N = int(input())

datas = list(map(int, input().split()))
max_data = 0
ans = 0

for data in datas:
    if data > max_data:
        max_data = data
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
    
print(ans)