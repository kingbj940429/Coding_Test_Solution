''' 11098번 첼시를 도와줘! '''

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        p = int(input())
        
        case_list = {}
        for _ in range(p):
            input_data = list(input().split(" "))
            case_list[input_data[0]] = input_data[1]
        max_key = 0        
        for key in case_list.keys():
            if(max_key < int(key)):
                max_key = int(key)
        print(case_list.get(str(max_key)))
