''' 2711번 오타맨 고창영 '''

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        #입력 값 한줄 씩 받는다
        input_data = input().split(" ")
        index = input_data[0]
        input_str = list(input_data[1])
        del(input_str[int(index)-1])
        print("".join(input_str))
        
        

        