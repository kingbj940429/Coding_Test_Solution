''' 8595번 히든 넘버 '''

#마지막 문자가 다 숫자일경우 반복문 안에 else 구문을 타지 않는다 => 이에 대한 처리 필요

def check_hidden_number(data):
    first_index = -1
    first_index_flag = False #첫번째 인덱스에 대한 체크 
    last_index = -1
    result_list = []
    for i in range(len(data)):
        if(data[i].isdigit() == True):
            if(first_index == -1 ):#처음으로 숫자가 나올때 체크해준다.
                first_index = i
        else:
            last_index = i
            if(first_index != -1):
                result_list.append(int(data[first_index:last_index]))
            first_index = -1
            last_index = -1

    return result_list



if __name__ == "__main__":
    N = input()
    input_data = input()
    input_data += "$"
    num_list = check_hidden_number(input_data)
    print(sum(num_list))

