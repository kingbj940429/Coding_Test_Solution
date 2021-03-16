''' 6996번 애너그램 '''

def set_word(word):
    result_dic ={}
    cnt = 0 
    for val in word:
        if(val not in result_dic):
            result_dic[val] = 0
        if(val in result_dic):
            result_dic[val] += 1

    return result_dic

def compare_A_B(A_dic,B_dic):
    flag = False
    for val in A_dic:
        if(val in B_dic):
            if(B_dic.get(val) != A_dic.get(val)):
                flag = True
                break
        else:
            flag = True
            break
    return flag



if __name__ == "__main__":
    N = int(input())
    
    for _ in range(N):
        input_data = input().split()
        A_dic = set_word(input_data[0]) 
        B_dic = set_word(input_data[1])
        flag = compare_A_B(A_dic, B_dic)

        #만들어진다면
        if(flag == False):
            print("%s & %s are anagrams."%(input_data[0], input_data[1]))
        else:
            print("%s & %s are NOT anagrams."%(input_data[0], input_data[1]))


