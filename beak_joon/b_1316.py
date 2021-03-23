''' 1316번 그룹 단어 체커 '''

if __name__ == "__main__":
    N = int(input())
    cnt = 0
    for i in range(N):
        input_data = input()
        temp_list = []
        flag = True
        if(len(input_data) > 1):
            for j in range(len(input_data) - 1):
                if(input_data[j] != input_data[j+1]):
                    temp_list.append(input_data[j])
            temp_list.append(input_data[j+1])
            for val in temp_list:
                if("".join(temp_list).count(val) > 1):
                    flag = False
            if(flag == True):
                cnt += 1
        else:
            cnt += 1
    print(cnt)
