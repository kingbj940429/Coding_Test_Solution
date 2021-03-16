''' 10769번 행복한지 슬픈지 '''

if __name__ == "__main__":
    input_data = input()

    happy_cnt = input_data.count(":-)")
    sad_cnt = input_data.count(":-(")
    
    if(happy_cnt > sad_cnt):
        print("happy")
    elif(sad_cnt > happy_cnt):
        print("sad")
    elif(sad_cnt == happy_cnt and happy_cnt>0 and sad_cnt>0):
        print("unsure")
    else:
        print("none")

