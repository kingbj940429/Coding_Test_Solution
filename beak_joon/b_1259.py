''' 1259번 팰린드롬수 '''

if __name__ == "__main__":
    
    while True:
        input_data = input()
        if(input_data == "0"):
            break
        
        reverse_data = input_data[::-1]

        if(reverse_data == input_data):
            print("yes")
        else:
            print("no")