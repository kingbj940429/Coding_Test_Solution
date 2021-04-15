''' 2495번 연속구간 '''

def continue_check(data):
    flag = False
    for i in range(len(data)-1):
        if(data[i] == data[i+1]):
            flag = True
            break

    return flag


if __name__ == "__main__":
    input_datas = []
    for _ in range(3):
        input_datas.append(input())
    
    for data in input_datas:
        if(continue_check(data) == True): #연속된 숫자가 있다면
            cnt = 1
            max_val = 0
            for i in range(0, len(data) - 1):
                if(data[i] == data[i+1]):
                    cnt += 1
                    if(cnt > max_val):
                        max_val = cnt
                else : 
                    cnt = 1
            print(max_val)
        else:
            print(1)