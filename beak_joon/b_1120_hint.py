''' 1120번 문자열 '''
''' 브루트 포스란, 단순무식하게 가능한 경우를 하나하나 대입해보는걸 뜻합니다. '''
if __name__ == "__main__":
    input_data = input().split(" ")

    X = input_data[0]
    Y = input_data[1]
    cnts = []
    for i in range(len(Y) - len(X) + 1):
        cnt = 0
        for j in range(len(X)):
            if(X[j] != Y[i+j]):
                cnt += 1
        cnts.append(cnt)
    print(min(cnts))

