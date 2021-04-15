''' 1475번 방 번호 '''

if __name__ == "__main__" :
    room_num = input()

    cnt = 1
    num_in_set = ['0','1','2','3','4','5','6','7','8','9']
    for num in room_num:
        if(num not in num_in_set):
            if(num=='6' and '9' in num_in_set):
                num_in_set.remove('9')
                continue
            elif(num=='9' and '6' in num_in_set):
                num_in_set.remove('6')
                continue
            else:
                cnt += 1
                num_in_set = ['0','1','2','3','4','5','6','7','8','9']
                num_in_set.remove(num)
        else:
            num_in_set.remove(num)
        


print(cnt)