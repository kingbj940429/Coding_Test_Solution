''' 17608번 막대기 '''

import sys
input = sys.stdin.readline

if __name__ == "__main__" : 
    N = int(input())
    datas = [int(input()) for _ in range(N)]


    max_value = 0
    cnt = 0

    while len(datas) > 0 :
        removed_data = datas.pop()
        if(removed_data > max_value):
            max_value = removed_data
            cnt +=1 

    print(cnt)
    
