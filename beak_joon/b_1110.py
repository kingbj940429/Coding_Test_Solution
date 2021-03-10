''' 1110번 더하기 사이클 '''

def sumFunction(num):
    num = addZero(num)
    num_list = list(map(int,num))

    sum_num = num_list[0] + num_list[1]

    sum_num = addZero(str(sum_num))
    sum_num_list = list(map(int,sum_num))

    new_num = str(num_list[-1]) + str(sum_num_list[-1])
    
    return new_num


def addZero(num):
    if(len(num)<2):
        num = "0" + num
    return num
    
    


if __name__ == "__main__":
    N = input()
    init_num = N
    cnt = 1
    new_num = N
    while True:
        new_num = sumFunction(new_num)
        if(int(new_num) == int(init_num)):
            print(cnt)
            break
        else:
            cnt += 1
            