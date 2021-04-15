''' UCPC는 무엇의 약자일까? '''

def check_UCPC(input_data):
    UCPC_dic = {}
    flag = True

    if(check_UCPC_order(input_data) == False):
        return False

    for val in UCPC:
        UCPC_dic[val] = input_data.count(val)
    
    for key in UCPC_dic.keys():
        if(UCPC_dic.get(key) < 0):
            flag = False
    if(UCPC_dic.get('C') < 2):
        flag = False
    return flag

def check_UCPC_order(input_data):
    upper_string = ""
    flag = True
    i=0
    for val in input_data:
        if(val == UCPC[i]):
            upper_string += val
            i+=1
        if(i==4):
            break
    if(upper_string.count("UCPC") < 1):
        flag = False

    return flag
        

UCPC = ['U', 'C', 'P', 'C']
if __name__ == "__main__":
    input_data = input()
    result = check_UCPC(input_data)
    if(result == True):
        print("I love UCPC")
    else:
        print("I hate UCPC")
