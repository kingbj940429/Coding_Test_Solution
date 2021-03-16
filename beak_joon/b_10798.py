''' 10798번 세로읽기 '''

if __name__ == "__main__":
    data_list = [input() for _ in range(5)]
    max_size = max([len(val) for val in data_list])
    result = ""
    
    for i in range(max_size):
        for j in range(5):
            if(i < len(data_list[j])):
                result += data_list[j][i]
    print(result)
            