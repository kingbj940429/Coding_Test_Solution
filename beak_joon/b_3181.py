''' 3181번 줄임말 만들기 '''

def check_word(input_data):
    flag = False
    result = ""
    for val in input_data:
        if(val in unnecessary_word and flag == False):
            flag = True
            result += val[0].upper()
        elif(val not in unnecessary_word):
            flag = True
            result += val[0].upper()
    return result

unnecessary_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
if __name__ == "__main__":
    input_data = list(input().split(" "))
    
    result = check_word(input_data)
    print(result)


