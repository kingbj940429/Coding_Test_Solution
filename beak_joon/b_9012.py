''' 9012번 괄호 '''

left_parent = ['(']
right_parent = [')']

def check_ps(input_data):
    is_ps = True
    left_parent_list = []

    for val in input_data:
        if(val in left_parent):
            left_parent_list.append(val)
        elif(val in right_parent):
            if(not left_parent_list):
                is_ps = False
                break
            elif(val == ')'):
                left_parent_list.pop()
    if(left_parent_list):
        is_ps = False

    return is_ps



if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        input_data = input()
        result = check_ps(input_data)
        print("NO" if result==False else "YES")
        