''' 8958번 OX퀴즈 '''

def checkCircle(char):
    flag = True
    if(char == "O"):
        flag = True
    else:
        flag = False

    return flag

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        input_data = input()
        input_len = len(input_data)

        continue_sum = 0
        j = 1

        for i in range(input_len):
            if(checkCircle(input_data[i]) == True):
                continue_sum += j
                j += 1
            else:
                j = 1

        print(continue_sum)


