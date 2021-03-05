''' 2386번 도비의 영어 공부 '''


if __name__ == "__main__":

    while True:
        input_list = list(input().split(" "))

        if(input_list[0] == "#"):
            break
        cnt = 0
        for i in range(1, len(input_list)):
            cnt += input_list[i].lower().count(input_list[0])
        print("%c %d"%(input_list[0], cnt))

    