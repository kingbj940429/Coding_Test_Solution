''' 1235번 학생 번호 '''

if __name__ == "__main__":
    N = int(input())

    number_list = []
    for _ in range(N):
        temp = input()#문자열도 받음
        number_list.append(temp[::-1])
    cnt = 0
    lastest = []

    for i in range(len(number_list)):
        for j in range(len(number_list[i])):
            if(number_list[i][j] not in lastest):
                lastest.append(number_list[i][j])
                
            else:
                cnt += 1
                break
    
    print(cnt)


            
        
            
            
        
