def get_chars_count(input_data):
    result_dic = {}
    removed_list = list(set(input_data))

    for val in removed_list:
        result_dic[val] = input_data.count(val)

    return result_dic



if __name__ == "__main__":
    input_data = input()
    chars_dic = get_chars_count(input_data)
    odd_cnt = 0
    odd_string = ""
    even_string = ""

    removed_list = sorted(list(set(input_data)))
    
    for val in removed_list:
        if(chars_dic.get(val) % 2 == 1):
            odd_cnt += 1
            odd_string += val
        even_string += val * (chars_dic.get(val) // 2)

    if odd_cnt > 1:
        print("sorry")
    else:
        print(even_string + odd_string + even_string[::-1])

