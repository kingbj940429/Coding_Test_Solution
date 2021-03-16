''' 9933번 민균이의 비밀번호 '''

def select_pw(data_list):
    for val in data_list:
        if(val[::-1] in data_list):
            result = val
    return result


if __name__ == "__main__":
    N = int(input())
    word_list = []
    for _ in range(N):
        temp = input()
        word_list.append(temp)

    pw = select_pw(word_list)
    middle_index = len(pw)//2

    print("%d %s"%(len(pw),pw[middle_index]))
    
