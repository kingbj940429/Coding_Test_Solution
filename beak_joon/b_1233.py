''' 1233번 주사위 '''

def get_max(sum_dic):
    max_val = 0
    for key in sum_dic.keys():
        if(sum_dic.get(key) > max_val):
            max_val = sum_dic.get(key)
    return max_val

if __name__ == "__main__" : 
    S1, S2, S3 = map(int,input().split())

    sum_dic = {}

    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                dice_sum = (i+j+k)
                if(dice_sum in sum_dic) : 
                    sum_dic[dice_sum] += 1
                else:
                    sum_dic[dice_sum]  = 0
    
    max_val = get_max(sum_dic)

    for key in sum_dic:
        if(sum_dic.get(key) == max_val):
            print(key)
            break

