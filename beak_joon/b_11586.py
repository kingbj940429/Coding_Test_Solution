''' 11586번 지영 공주님의 마법 거울 '''

def original_list(data_list, N):
    for i in range(N):
        for j in range(N):
            print(data_list[i][j], end="")
        print("")

def right_left_list(data_list, N):
    for i in range(N):
        for j in range(N-1,-1,-1):
            print(data_list[i][j], end="")
        print("")    

def up_down_list(data_list, N):
    for i in range(N-1,-1,-1):
        for j in range(N):
            print(data_list[i][j], end="")
        print("")

if __name__ == "__main__":
    N = int(input())
    data_list = [list(input()) for _ in range(N)]
    K = int(input())

    #그대로
    if(K==1):
        original_list(data_list, N)
    #좌우반전
    elif(K==2):
        right_left_list(data_list, N)
    #상하반전
    elif(K==3):
        up_down_list(data_list, N)


