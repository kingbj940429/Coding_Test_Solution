''' 1021번 회전하는 큐 '''
from collections import deque

def second_que(datas):
    temp = datas.popleft()
    datas.append(temp)

    return datas

def third_que(datas):
    temp = datas.pop()
    datas.appendleft(temp)

    return datas


if __name__ == "__main__":
    N, M = map(int,input().split())
    idxs = list(map(int,input().split()))
    datas = deque([ i  for i in range(1,N+1)])
    cnt = 0
    
    for idx in idxs:
        while True:
            if(datas[0] == idx):
                datas.popleft()
                break
            index = datas.index(idx) + 1
            diff_back = abs(len(datas) - index + 1)
            diff_front = index
            #세번째 방법
            if(diff_front > diff_back):
                datas = third_que(datas) 
                cnt += 1
            #두번째 방법
            else:
                datas = second_que(datas)
                cnt += 1
    print(cnt)





