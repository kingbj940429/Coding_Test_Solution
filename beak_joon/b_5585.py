''' 5585번 거스름돈 '''

money_list = [500, 100, 50, 10, 5, 1]
money = 1000
charge_money = int(input())

diff_money = money - charge_money
cnt = 0
for val in money_list:
    cnt += diff_money // val
    diff_money %= val

print(cnt)


