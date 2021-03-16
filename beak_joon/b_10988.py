''' 10988번 팰린드롬인지 확인하기 '''

if __name__ == "__main__":
    input_data = input()
    reverse_data = input_data[::-1]
    if(reverse_data == input_data):
        print(1)
    else:
        print(0)