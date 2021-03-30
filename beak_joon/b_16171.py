''' 16171번 나는 친구가 적다 '''

def remove_digit(input_data):
    result = ""
    for val in input_data:
        if(val.isdigit() == False):
            result += val
    return result


if __name__ == "__main__":
    input_data = input()
    find_data = input()

    remove_digit_data = remove_digit(input_data)

    if(remove_digit_data.count(find_data) > 0 ):
        print(1)
    else:
        print(0)

    