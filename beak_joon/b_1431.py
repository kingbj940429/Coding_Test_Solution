''' 1431번 시리얼 번호 '''
import sys
input = sys.stdin.readline

def serial_sum(serial):
    sum_val = 0
    for i in range(len(serial)):
        if serial[i].isdigit() == True:
            sum_val += int(serial[i])
    return sum_val


N = int(input().rstrip())

serial = []
for _ in range(N):
    serial.append(input().rstrip())

# 시리얼번호, 시리얼 번호 길이, 시리얼 번호 숫자 합
for i in range(len(serial)):
    temp_se = serial[i]
    serial[i] = ([temp_se, len(temp_se),serial_sum(temp_se)])

serial.sort(key=lambda x : (x[1],x[2],x[0]))
for i in serial:
    print(i[0])

