''' 2941번 크로아티아 알파벳 '''

def get_cro_word_count(input_data):
    cnt = 0
    for val in croatia_chars:
        if(val in input_data):
            cnt += input_data.count(val)    
            input_data = input_data.replace(val," ")
    cnt += rest_word_count(input_data.replace(" ", ""))
    return cnt

def rest_word_count(input_data):
    return len(input_data)


croatia_chars = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
if __name__ == "__main__":
    cro_cnt = 0
    input_data = input()

    cro_cnt = get_cro_word_count(input_data)
    print(cro_cnt)




