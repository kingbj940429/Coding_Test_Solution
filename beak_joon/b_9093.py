''' 9093번 단어 뒤집기 '''

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        result = ""
        input_data = list(input().split(" "))
        for val in input_data:
            result += val[::-1] + " " 
        print(result.rstrip())


        
        