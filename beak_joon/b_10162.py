''' 10162번 전자레인지 '''

time_list = [300, 60, 10]
if __name__ == "__main__" : 
    N = int(input())

    if(N%10 !=0):
        print("-1")
    else:
        cnt = 0
        i = 0
        per_list = []

        for time in time_list:
            per_cnt = N // time
            per_list.append(per_cnt)
            N = N%time

        print(per_list[0], end=' ')
        print(per_list[1], end=' ')
        print(per_list[2], end=' ')

    
    





