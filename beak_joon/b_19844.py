''' 19844번 단어 개수 세기 '''
front_word = ['c','j','n','m','t','s','l','d','qu','s']
mother_word = ['a','e','i','o','u','h']

if __name__ == "__main__":
    input_data = input()
    
    input_data = " ".join(input_data.split("-"))
    input_data = input_data.split(" ")

    include_list = []
    not_include_list = []
    print(input_data)
    for word in input_data :
        if(word.find("'") > 0):
            include_list.append(word.split("'"))
        else:
            not_include_list.append(word)
    print(not_include_list)
    print(include_list)
    print("============")
    minus_cnt = 0
    result_list = []
    for val in include_list:
        combine_val = "'".join(val)
        for index in range(len(combine_val)):
            if(combine_val[index] == "'" ):
                if(combine_val[index-1] == 'u' and combine_val[index - 2] !='q'):
                        minus_cnt += 1
                else:
                    if(combine_val[index - 1] not in front_word or combine_val[index + 1] not in mother_word):
                        minus_cnt += 1
            
    print(minus_cnt)


    



