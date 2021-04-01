''' 4949번 균형잡힌 세상 '''

left_parent = ['(', '[']
right_parent = [')', ']']
if __name__ == "__main__":
    while True:
        left_parent_list = []
        is_flag = True
        input_data = input()
        if(len(input_data)<2 and input_data.find(".") > -1):
            break
        
        for val in input_data:
            if(val in left_parent):
                left_parent_list.append(val)
            elif(val in right_parent):
                # left 스택에 아무것도 없는데 right가 있다? 무조건 No
                if(not left_parent_list):
                    is_flag = False
                    break
                # right가 나오고 스택에 하나 이상의 값이 담겨있다.
                elif(left_parent_list):
                    if(val == ')' and left_parent_list[-1] == '('):
                        left_parent_list.pop()
                    elif(val == ']' and left_parent_list[-1] == '['):
                        left_parent_list.pop()
                    else:
                        is_flag = False
                        break
        if(left_parent_list):
            is_flag = False
        if(is_flag == True):
            print("yes")
        else:
            print("no")


        

