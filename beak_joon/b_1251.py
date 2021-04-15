''' 1251번 단어 나누기 '''
'''
1. 가장 빠른 알파벳 3개를 고른다.
2. 3개의 알파벳 기준으로 문자열을 3등분으로 나눈다.
3. 3등분한 문자열을 뒤집고 합친다.
'''

def asc_data_top3(data_list):
    for i in range(3):
        data_top3.append(data_list[i])

def slice_data_for_top3(data_list):
    temp = ""
    result_list = []
    for val in data_list:
        temp += val
        print(temp)
        if(val in data_top3):
            result_list.append(temp[::-1])
            temp = ""
    
    return result_list

data_top3 = []
if __name__ == "__main__" :
    input_data = input()
    data_list = list(input_data)
    data_list.sort(key=lambda x : x[0])

    asc_data_top3(data_list)
    print(slice_data_for_top3(input_data))

    
