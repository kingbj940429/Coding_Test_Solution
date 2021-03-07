''' 2577번 숫자의 개수 '''

def subDatas(input_datas) : 
    result = 1
    for data in input_datas:
        result *= int(data)
    return str(result)

if __name__ == "__main__" :
    input_datas = [ input() for _ in range(3)]
    sub_data = list(subDatas(input_datas))
    result_dic = {}

    #각 숫자에 대한 카운트 0으로 담기
    for i in range(10):
        result_dic[i] = 0
    
    for k in range(len(sub_data)):
        result_dic[int(sub_data[k])] += 1
    
    for key in result_dic.keys():
        print(result_dic.get(key))


