''' 5656번 비교 연산자 '''

def gtFunc(left_num, right_num):
    if(left_num > right_num):
        return True
    else:
        return False
def geFunc(left_num, right_num):
    if(left_num >= right_num):
        return True
    else:
        return False
def ltFunc(left_num, right_num):
    if(left_num < right_num):
        return True
    else:
        return False        
def leFunc(left_num, right_num):
    if(left_num <= right_num):
        return True
    else:
        return False
def eqFunc(left_num, right_num):
    if(left_num == right_num):
        return True
    else:
        return False
def neFunc(left_num, right_num):
    if(left_num != right_num):
        return True
    else:
        return False                

if __name__ == "__main__":
    cnt = 1
    while True:
        input_data = list(input().split(" "))
        left_num = int(input_data[0])
        right_num = int(input_data[2])
        compare = input_data[1]
        flag = False
        
        if(compare == ">"):
            flag = gtFunc(left_num, right_num)
        elif(compare == ">="):
            flag = geFunc(left_num, right_num)
        elif(compare == "<"):
            flag = ltFunc(left_num, right_num)
        elif(compare == "<="):
            flag = leFunc(left_num, right_num)
        elif(compare == "=="):
            flag = eqFunc(left_num, right_num)
        elif(compare == "!="):
            flag = neFunc(left_num, right_num)
        else:
            break
        print("Case %d: %s"%(cnt, str(flag).lower()))
        cnt += 1
