''' 1789번 수들의 합 '''
N = int(input())
result = 0
cnt = 0
i = 1
while True:
    result += i
    i += 1
    if result > N:
        break
    cnt += 1
print(cnt)

