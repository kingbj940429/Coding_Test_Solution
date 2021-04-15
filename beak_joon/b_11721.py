''' 11721번 열 개씩 끊어 출력하기 '''

if __name__ == "__main__":
    N = input()

    count = 0
    result = ""
    
    rest_value = len(N)%10

    for i in range(len(N) - rest_value):
        result += N[i]
        count += 1
        
        if(count == 10):
            print(result)
            result = ""
            count = 0
    
    for i in range(len(N) - rest_value, len(N)):
        result += N[i]
    print(result)
