''' 1213번 팰린드롬 만들기 '''

'''
팰린드롬 팁
1. 홀수인 문자는 무조건 1개 이하로 와야함. 만약, 2개 이상이라면 절대 팰린드롬이 될수 없음
2. 반으로 자르고 왼쪽짝수문자 + 1개이하인 홀수문자 + 오른쪽짝수문자 이런식으로 연결하면 편함
'''

def count_chars(input_data):
    result_dic = {}
    removed_list = list(set(input_data))

    for val in removed_list:
        result_dic[val] = input_data.count(val)
    return result_dic

if __name__ == "__main__":
    input_data = input()
    count_chars_dic = {}
    odd_cnt = 0
    odd_char = ""
    even_string = ""
    count_chars_dic = count_chars(input_data)#알파벳의 갯수를 센다
    chars_list = []

    for key in count_chars_dic.keys():
        chars_list.append(key)

    chars_list.sort()
    for val in chars_list:
        if(count_chars_dic.get(val) % 2 == 1):
            odd_cnt += 1
            odd_char += val
        even_string += val * (count_chars_dic.get(val) // 2)
    if odd_cnt > 1:
        print("I'm Sorry Hansoo")
    else:
        print(even_string + odd_char + even_string[::-1])


    



