''' 1769번 3의 배수 '''

def data_sum(input_data):
    result = 0
    for val in input_data:
        result += int(val)
    return result

if __name__ == "__main__":
    input_data = list(input())
    cnt = 1
    total_sum = data_sum(input_data)
    
    if(len(input_data) <= 1):
        cnt = 0

    while len(str(total_sum)) > 1:
        sum_list = list(str(total_sum))
        total_sum = data_sum(sum_list)
        cnt += 1


    print(cnt)
    if(total_sum%3 != 0):
        print("NO")
    else:
        print("YES")



        
    


    


    
