''' 2744번 대소문자 바꾸기 '''

if __name__ == "__main__":
    input_data = input()
    result = ""
    for val in input_data:
        if(val.islower() == True):
            result += val.upper()
        else:
            result += val.lower()
    print(result)