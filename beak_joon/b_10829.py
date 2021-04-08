''' 10829번 이진수 변환 '''

if __name__ == "__main__":
    N = int(input())

    result = ""
    while N > 0:
        num = N%2
        result +=str(num)
        N //= 2
    print(result[::-1])
    

