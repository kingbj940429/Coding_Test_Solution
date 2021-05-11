''' 5671번 호텔 방 번호 '''

def solution(N, M):
    cnt = 0

    for i in range(N, M + 1):
        i_str = str(i)
        flag = True
        num_dic = {}
        for i in range(0, 10):
            num_dic[str(i)] = 0

        for j in i_str:
            num_dic[j] += 1
            if num_dic[j] > 1:
                flag = False
                break
        if flag == True:
            cnt += 1

    return cnt


while True:
    try :
        N, M = map(int,input().split())
        print(solution(N, M))
    
    except EOFError:
        break