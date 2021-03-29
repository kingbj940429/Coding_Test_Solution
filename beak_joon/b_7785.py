''' 7785번 회사에 있는 사람 '''

if __name__ == "__main__" :
    N = int(input())

    result_dic = {}

    for _ in range(N):
        input_data = input().split()
        name = input_data[0]
        status = input_data[1]
        result_dic[name] = status

    result_list = []
    for key in result_dic.keys():
        if(result_dic.get(key) == 'enter'):
            result_list.append(key)
    result_list.sort(reverse=True)
    
    for val in result_list:
        print(val)

    


