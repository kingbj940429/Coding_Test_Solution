''' 1235번 학생 번호 '''

if __name__ == "__main__" : 
    N = int(input())

    student_ids = []
    for _ in range(N):
        temp = input()
        student_ids.append(temp)
    #학생 번호의 길이
    id_len = len(student_ids[0])

    cnt = 0
    
    for i in range(id_len-1,-1,-1):
        temp_list = []
        same_cnt = 0
        for id in student_ids:
            #만약 없으면 임시 리스트에 계속 넣어준다.
            if("".join(id[i:]) not in temp_list):
                temp_list.append("".join(id[i:]))
                same_cnt += 1
            #만약 있으면 겹치는 것이므로 다음 인덱스로 넘어간다.
            else:
                cnt += 1
                break
        if(same_cnt == N ):
            print(id_len-i)
            break
    
            


