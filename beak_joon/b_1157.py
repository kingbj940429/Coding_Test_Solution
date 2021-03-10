''' 1157번 단어 공부 '''

if __name__ == "__main__":
    input_str = input()
    input_str = input_str.upper()

    str_set = set(input_str)
    result_dic = {}
    result_char = ""
    max_num = 0

    for char in str_set:
        result_dic[char] = input_str.count(char)
        if(input_str.count(char) > max_num):
            max_num = input_str.count(char)
            result_char = char
    check_cnt=0
    for char in str_set :
        if(max_num == result_dic.get(char)):
            check_cnt += 1
    
    if(check_cnt>=2):
        print("?")
    else:
        print(result_char)
    
    


