''' 2902번 KMP는 왜 KMP일까? '''

if __name__ == "__main__":
    input_data = input()
    result = ""
    for char in input_data:
        if(char.isupper() == True):
            result += char

    print(result)

