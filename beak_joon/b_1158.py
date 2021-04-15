''' 1158번 요세푸스 '''

if __name__ == "__main__":
    N, K = map(int,input().split())
    
    #데이터 초기화
    datas = [ i for i in range(1,N+1)]

    index = 0
    result = []
    
    while len(datas) > 0 :

        #데이터 하나가 빠지니깐 K-1를 해준다.
        index += (K-1)

        if(index >= len(datas)):
            index  = index%len(datas)
        result.append(str(datas.pop(index)))
    
    print("<",", ".join(result)[:],">", sep='')