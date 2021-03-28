''' 3568번 iSharp '''

def remove_comma(input_data):
    result_list = []
    for val in input_data:
        if(val.find(",") > 0):
            val = val.replace(",","")
        result_list.append(val)
    return result_list

            
basic_type = ['[]', '&', '*']
if __name__ == "__main__" : 
    input_data = input()

    input_data = input_data.split(" ")
    removed_comma_data = remove_comma(input_data)
    
    common_data_type = removed_comma_data[0]#공통 변수형 선언
    removed_comma_data.remove(common_data_type)#리스트에서 공통 변수형 제거
