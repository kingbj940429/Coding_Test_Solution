''' 큰 수의 법칙 '''

if __name__ == "__main__":
    input_data = input().split(" ")

    N = input_data[0]
    M = input_data[1]
    K = input_data[2]

    data_list = input().split(" ")
    data_list.sort(reverse=True)
    
    k ,result = 0, 0
    for i in range(int(M)):
        if((i+1)%int(K) == 0):
            result += int(data_list[k+1])
        else:
            result += int(data_list[k])
    print(result)


