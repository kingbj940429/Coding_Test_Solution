''' 2857번 FBI '''

if __name__ == "__main__":
    index_list = []

    for i in range(5):
        input_name = input()
        if(input_name.find("FBI") > -1):
            index_list.append(i+1)
    index_list.sort()

    if(len(index_list) > 0):
        for val in index_list:
            print(val, end=" ")
    else:
        print("HE GOT AWAY!")
