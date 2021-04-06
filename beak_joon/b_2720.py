''' 2720번 세탁소 사장 동혁 '''

#동전
money_list = [25,10,5,1]

N = int(input())

for _ in range(N):
    data = int(input())
    per_cnt_list = []

    for money in money_list:
        per_cnt = data // money
        per_cnt_list.append(per_cnt)
        data = data%money
    
    for val in per_cnt_list:
        print(val, end=' ')
