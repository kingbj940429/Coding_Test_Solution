''' 그리디알고리즘 : 숫자 카드 게임 '''
if __name__ == "__main__":
    N, M = map(int,input().split())

    data_list = []
    for _ in range(N):
        temp_data = list(map(int,input().split()))
        data_list.append(temp_data)

    min_list = []
    for datas in data_list:
        min_list.append(min(datas))
        
    print(max(min_list))
