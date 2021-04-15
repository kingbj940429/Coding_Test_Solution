''' 2161번 카드1 '''

from collections import deque
if __name__ == "__main__" : 
    #반복횟수 홀수면 버리고 짝수면 뒤로
    cnt = 1

    N = int(input())

    removed_datas = []
    #N까지 리스트 만들어줌
    datas = []
    for i in range(N, 0, -1):
        datas.append(i)
    datas = deque(datas)

    while len(datas) > 0 :
        #홀수
        if(cnt%2 != 0):
            removed_datas.append(datas.pop())

        #짝수
        else:
            #맨 위 카드를 다시 맨 뒤로
            datas.appendleft(datas.pop())
        cnt += 1
    
    for val in removed_datas:
        print(val,end=' ')

