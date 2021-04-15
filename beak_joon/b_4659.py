''' 4659번 비밀번호 발음하기 '''

def check_have_mother_chars(input_data):
    flag = False

    for val in input_data:
        if(val in mother_chars):
            flag = True

    return flag

def check_countinue_three_chars(input_data):
    flag = True
    mother_cnt = 0#모음
    child_cnt = 0#자음

    for i in range(len(input_data)):
        if(input_data[i] in mother_chars):
            mother_cnt += 1
            child_cnt = 0
        elif(input_data[i] not in mother_chars):
            child_cnt += 1
            mother_cnt = 0 

        if(child_cnt == 3 or mother_cnt == 3):
            flag = False
            break
    return flag

def check_double_chars(input_data):
    flag = True

    for i in range(len(input_data) - 1):
        if(input_data[i] == input_data[i+1]):
            temp_data = input_data[i] + input_data[i+1]
            if(temp_data not in possible_double_chars):
                flag = False
                break

    return flag

mother_chars = ['a', 'e', 'i', 'o', 'u']
possible_double_chars = ['ee', 'oo']
if __name__ == "__main__" : 
    while True:
        input_data = input()
        is_three_chars = False
        is_double_chars = False
        is_have_chars = False

        if(input_data == 'end'):
            break

        #로직 시작
        is_have_chars = check_have_mother_chars(input_data)
        if(is_have_chars == False):
            print("<"+ input_data + ">" + " is not acceptable.")
            continue
        is_three_chars = check_countinue_three_chars(input_data)
        if(is_three_chars == False):
            print("<"+ input_data + ">" + " is not acceptable.")
            continue
        is_double_chars = check_double_chars(input_data)
        if(is_double_chars == False):
            print("<"+ input_data + ">" + " is not acceptable.")
            continue
        print("<"+ input_data + ">" + " is acceptable.")
        
