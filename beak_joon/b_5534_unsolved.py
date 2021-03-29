''' 5534번 간판 '''
'''
해결못함


1. diff_index로 data[diff_index]에 간판이름이 있는지 체크 
2. 하나라도 없으면 예외처리
'''

def check_possible_board(input_data):
    #간격을 체크해주기 위한
    diff_index = 0

    get_diff_index(input_data)


def get_diff_index(input_data):
    diff_index = 0
    temp_chars = []
    first_index = 0
    cnt = 0
    k = 0

    while True:
        for i in range(len(board_name)):
            for j in range(k ,len(input_data)):
                if(board_name[i] == input_data[j]):
                    if(i==0):
                        first_index = j
                    temp_chars.append(j)
                    k = j
                    cnt += 1
                    break
                if(cnt == 2):
                    break
        diff_index = temp_chars[1] - temp_chars[0]

        for i in range(len(board_name)):
            if()


    
        

    

            



    return False
board_name = ""
if __name__ == "__main__":
    N = int(input())
    board_name = input()

    for _ in range(N):
        is_board = False
        input_data = input()

        is_board = check_possible_board(input_data)

