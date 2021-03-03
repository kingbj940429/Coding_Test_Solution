''' 1264번 모음의 개수'''

moum = ['a','e','i','o','u']

def count_lower(string):
    temp_cnt = 0
    str_len = len(string)
    for i in range(str_len):
        if(string[i].lower() in moum):
            temp_cnt += 1
    print(temp_cnt)

if __name__ == "__main__":
    while True:
        input_data = input()
        if(input_data == "#"):
            break
        count_lower(input_data)
    

        
        

    