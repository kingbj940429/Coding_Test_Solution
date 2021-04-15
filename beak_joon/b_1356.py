''' 1356번 유진수 '''

if __name__ == "__main__":
    input_data = input()

    data_len = len(input_data)
    start = 0
    end = data_len
    flag = False
    for i in range(1,data_len):
        left = input_data[0:i]
        right = input_data[i:end]
        left_val = 1
        right_val = 1
        for i in left:
            left_val *= int(i)
        for j in right:
            right_val *= int(j)
        if(left_val == right_val):
            flag=True
    if(flag == True):
        print("YES")
    else:
        print("NO")

        

