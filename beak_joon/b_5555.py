''' 5555번 반지 '''

if __name__ == "__main__" :
    ring_word = input()
    N = int(input())   
    cnt = 0

    for _ in range(N):
        input_data = input()
        input_data += input_data
        if(ring_word in input_data):
            cnt += 1
    print(cnt)
