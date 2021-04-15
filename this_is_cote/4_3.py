''' 4-3 왕실의 나이트 '''
'''
접근방법
1) 상하좌우로 나눠서 계산
2) 첫번째 움직이고 상하좌우에 대한 경우의 수 계산
'''


input_data = list(input())

#소문자인 좌표를 숫자로 변경하기
x = int(input_data[1])
y = ord(input_data[0]) - ord('a') + 1
#숫자로만 좌표 구성
pos = [x,y]

steps = [[-2,-1], [-1,-2], [1,-2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
cnt = 0
for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if dx >= 1 and dx <=8 and dy >= 1 and dy <= 8:
        cnt += 1
print(cnt)


