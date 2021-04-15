''' 10773번 제로 '''

if __name__ == "__main__":
    K = int(input())

    digit_list = []

    for _ in range(K):
        temp = int(input())
        if(temp != 0):
            digit_list.append(temp)
        else:
            digit_list.pop()
        
    print(sum(digit_list))
