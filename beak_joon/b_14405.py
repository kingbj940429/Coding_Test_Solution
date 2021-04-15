''' 14405번 피카츄 '''

def remove_static_word(input_data):
    for val in static_word:
        while val in input_data:
            input_data = input_data.replace(val, "#")
    return input_data

static_word = ['pi', 'ka', 'chu']
if __name__ == "__main__":
    input_data = input()
    is_check = True
    removed_data = remove_static_word(input_data)

    for val in removed_data:
        if(val != '#'):
            is_check = False
            break

    if(is_check == True):
        print("YES")
    else:
        print("NO")