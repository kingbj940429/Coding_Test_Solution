''' 10820번 문자열 분석 '''

while True:
    try:
        data = list(input())
        lower = 0
        upper = 0
        num = 0
        space = 0

        for i in data :
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isdigit():
                num += 1
            elif i.isspace():
                space += 1
        print(lower, upper, num, space)
    except EOFError :
        break