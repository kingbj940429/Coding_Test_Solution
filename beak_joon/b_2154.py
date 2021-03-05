''' 2154번 수 이어 쓰기 3 '''

def whole_number(N):
    result = ""
    for i in range(1,int(N)+1):
        result += str(i)
    return result

if __name__ == "__main__":
    N = input()
    numbers = whole_number(N)#1~N까지의 수 잇기
    print(numbers.find(N) + 1)