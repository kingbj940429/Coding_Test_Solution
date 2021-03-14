''' 10987번 모음의 개수 '''

parent_letters = ['a','e','i','o','u']

if __name__ == "__main__":
    input_data = input()
    cnt = 0
    for val in input_data:
        if(val in parent_letters):
            cnt +=1
    print(cnt)

