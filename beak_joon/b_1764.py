''' 1764번 듣보잡 '''

if __name__ == "__main__":
    N, M = map(int,input().split(" "))


    N_data = [input() for _ in range(N)]
    M_data = [input() for _ in range(M)]

    N_set = set(N_data)
    M_set = set(M_data)

    result_list = list(M_set & N_set)
    result_list.sort()

    print(len(result_list))
    
    for val in result_list:
        print(val)
    
        