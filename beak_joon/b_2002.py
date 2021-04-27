''' 2002번 추월 '''
# 차의 대수
N = int(input())

#들어가는 차, 나오는 차
in_car = []
out_car = []
for i in range(N):
    temp = input()
    in_car.append(temp)

for i in range(N):
    temp = input()
    out_car.append(temp)

# 추월한 차 확인
cnt = 0
while len(out_car) > 0 :
    car = out_car[0]
    in_idx = in_car.index(car)
    out_idx = out_car.index(car)

    if in_idx != out_idx :
        cnt += 1
        in_car.pop(in_idx)
        out_car.pop(out_idx)
    else:
        in_car.pop(in_idx)
        out_car.pop(out_idx)

print(cnt)






