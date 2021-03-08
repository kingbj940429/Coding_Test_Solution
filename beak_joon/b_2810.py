''' 2810번 컵홀더 '''

def couple_index(result_data):
    data_len = len(result_data)
    index = []
    check_cnt = 0
    for i in range(0, data_len):
        if(result_data[i] == "L"):
            check_cnt += 1
            if(check_cnt == 2):
                index.append(i-1)
                check_cnt = 0
    return index

if __name__ == "__main__":
    N = int(input())
    input_data = input()

    result_data = ""
    for i in range(N):
        result_data += "*" + input_data[i]
    #print(result_data)
    indexs = couple_index(result_data)
    result_data = list(result_data)
    
    real_result = []
    for i in range(len(result_data)):
        if(i not in indexs):
            real_result.append(result_data[i])
    result = "".join(real_result) + "*"
    if(result.find("L")<0):
        print(result.count("S"))
    else:
        #print(result)
        print(result.count("*"))


    
    


    