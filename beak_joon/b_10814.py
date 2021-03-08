''' 10814번 나이순 정렬 '''

if __name__ == "__main__":
    N = int(input())
    input_data = []

    for _ in range(N):
        temp_data = input().split()
        input_data.append(temp_data)
    
    input_data.sort(key=lambda x :(x[0]))
    
    for i in range(N):
        print("%s %s"%(input_data[i][0], input_data[i][1]))