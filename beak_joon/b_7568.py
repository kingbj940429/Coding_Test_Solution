''' 7568번 실버V '''


N = int(input())
people = []

#입력값 키 몸무게로 담는다.
for _ in range(N):
    temp_list = []
    w, h = map(int,input().split())
    temp_list.append(w)
    temp_list.append(h)
    people.append(temp_list)

#비교해준다.
for per1 in people:
    cnt = 1
    for per2 in people:
        if(per1[0] < per2[0] and per1[1] < per2[1]):
            cnt += 1
    print(cnt , end = ' ')