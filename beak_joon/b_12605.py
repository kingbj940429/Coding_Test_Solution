''' 12605번 단어순서 뒤집기 '''

if __name__ == "__main__" : 
    N = int(input())

    for i in range(1, N+1):
        datas = input().split(" ")
        datas.reverse()
        result = " ".join(datas)
        print("Case #" + str(i)+": "+result)