''' 14490번 백대열 '''

def gcd(x,y):
    while y:
        x, y = y, x%y        
    return x

if __name__ == "__main__":
    input_data = input()
    num_list = input_data.split(":")

    gcd_num = int(gcd(int(num_list[0]), int(num_list[1])))
    result = str(int(num_list[0])//gcd_num)+ ":" + str(int(num_list[1])//gcd_num)
    print(result)

