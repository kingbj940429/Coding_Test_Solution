''' 2954번 창영이의 일기장 '''

def checkP(input_data):
    result = ""
    for letter in check_letters:
        first_letter = letter[0]
        if(letter in input_data):
            input_data = input_data.replace(letter, first_letter)

    return input_data

check_letters = ['apa','epe','ipi','opo','upu']
if __name__ == "__main__":
    input_data = input()
    result = checkP(input_data)
    print(result)
    


