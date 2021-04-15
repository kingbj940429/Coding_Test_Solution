''' 11091번 알파벳 전부 쓰기 '''

def set_alpha():
    start_alpha_asci = ord('a')
    last_alpha_asci = ord('z')
    alpha = []

    for i in range(start_alpha_asci, last_alpha_asci + 1):
        alpha.append(chr(i))

    return alpha

def not_pangram_list(data_list):
    result = ""
    for val in alpha_list:
        if(val not in data_list):
            result += val
    return result
            

alpha_list = set_alpha()
if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        result_list =[]
        input_data = input()
        input_data = input_data.lower().replace(" ", "")

        for val in input_data:
            if(val in alpha_list):
                result_list.append(val)
        result_list = list(set(result_list))
        result_list.sort()

        result_str = not_pangram_list(result_list)
        
        if(len(result_str) == 0):
            print("pangram")
        else:
            print("missing " + "".join(result_str))
