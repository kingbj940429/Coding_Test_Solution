''' 1924번 2007년 '''

months = {'1' : 31, '2' : 28, '3' : 31, '4' : 30, '5' : 31, '6' : 30, '7' : 31, '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31}
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

datas = input().split()
x = datas[0]
y = datas[1]

#전월까지 일수 구하기
cnt = 0
for key in months.keys():
    if(x == key):
        break
    cnt += months.get(key)

#현재 달의 날짜 계산
cnt += int(y)
cnt = int(cnt)%7

print(days[cnt])

