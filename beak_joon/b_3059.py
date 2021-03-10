''' 3059번 등장하지 않는 문자의 합 '''

def set_alpha():
    start = ord("A")
    end = ord("Z")

    for i in range(start, end + 1):
        alpha[chr(i)] = i         

alpha = {}
if __name__ == "__main__":
    set_alpha()
    N = int(input())

    for i in range(N):
        input_str = input()
        result = 0
        for key in alpha.keys():
            if(key not in input_str):
                result += int(alpha.get(key))
        print(result)
