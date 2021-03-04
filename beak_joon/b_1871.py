''' 백준 1871번 좋은 자동차 번호판 '''

def alpha_value(input_data):
    value = 0
    j = 2
    for i in range(0, 3):
        alpha_ord = ord(input_data[i]) - ord("A")
        value = value + alpha_ord * 26 ** j
        j -=1
    return value


def number_value(input_data):    
    value = []
    for i  in range(4,len(input_data)):
        value.append(input_data)
    return int(input_data[4::])

if __name__ == "__main__":
    N = int(input())
    
    for _ in range(N):
        input_data = input()
        value_diff = abs(alpha_value(input_data) - number_value(input_data))
        if(value_diff <= 100):
            print("nice")
        else:
            print("not nice")