''' 11899번 괄호 끼어넣기 '''

if __name__ == "__main__" : 
    datas = list(input())

    left = [] # (
    right = [] # )
    cnt = 0
    for data in datas :
        if(data == '('):
            left.append(data)
        else:
            if(len(left) > 0 ):
                left.pop()
            else:
                cnt += 1
    
    print( cnt + len(left))
