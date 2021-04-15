''' 20112번 사토르 마방진 '''


if __name__ == "__main__":
    N = int(input())
    flag = True
    input_data = [list(input()) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if(input_data[i][j] != input_data[j][i]):
                flag = False
    if(flag == False):
        print("NO")
    else:
        print("YES")