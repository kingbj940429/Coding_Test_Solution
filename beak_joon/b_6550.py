''' 6550번 부분 문자열 '''

if __name__ == "__main__":
    while True:
        try:
            input_data = input().split(" ")

            s = input_data[0]
            t = input_data[1]

            data_list = []
            temp = ""
            for val in t :
                if(val in s):
                    temp +=val
                    
            if(s in temp):
                print("Yes")
            else:
                print("No")
            
        except EOFError:
            break