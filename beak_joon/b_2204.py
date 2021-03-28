''' 2204번 도비의 난독증 테스트 '''

if __name__ == "__main__":
    while True:
        N = int(input())
        if(N == 0):
            break

        word_list = []
        for i in range(N):
            data = input()
            word_list.append(data)
        word_list.sort(key=lambda x : x.lower())
        print(word_list[0])
        
