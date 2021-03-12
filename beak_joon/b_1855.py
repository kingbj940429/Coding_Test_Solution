''' 1855번 암호 '''

def setList(input_list, data_list):
    k = 0 
    for i in range(0, len(data_list)):
        for j in range(0, len(data_list[i])):
            data_list[i][j] = input_list[k]
            k += 1
    return data_list


def encrypt(set_list, col, row):
    result = ""
    for i in range(col):
        for j in range(row):
            result += set_list[j][i]
    print(result)

if __name__ == "__main__":
    K = int(input())# 열
    input_list = input()# 행
    M = len(input_list)//K
    
    data_list = [[0] * K for i in range(M)]
    set_list = setList(input_list, data_list)
    
    #메시지 받았을 때 예시처럼 배열 정렬
    for i in range(len(set_list)):
        if(i%2 != 0):
            set_list[i]=set_list[i][::-1]
            

    encrypt(set_list, K, M)

