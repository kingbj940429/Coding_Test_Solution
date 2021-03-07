''' 2596번 비밀편지 '''

sec_char = {'A':'000000','B' : '001111',
         'C':'010011','D': '011100',
         'E':'100110','F':'101001',
         'G':'110101','H':'111010'}
# key 값 가져오기
def DiffChar(input_str):
    for key in sec_char.keys():
        diff_cnt = 0
        val = sec_char.get(key)#val key : 000000 A
        for i in range(len(val)):
            if(val[i] != input_str[i]):
                diff_cnt += 1
        if(diff_cnt < 2):
            return key 

if __name__ == "__main__":
    N = int(input())
    input_data = input()
    result = ""
    flag = False
    #6자리씩 자르기
    for i in range(N):
        key = DiffChar(input_data[6*i:6*(i+1)])
        if(key == None):
            print(i+1)
            flag = True
            break
        else:
            result += key
    if(flag == False):
        print(result)