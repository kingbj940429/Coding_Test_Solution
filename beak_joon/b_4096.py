''' 4096번 팰린드로미터 '''

def felindrom_check(input_data):
    is_felindrom = True
    data_len = len(input_data)

    for i in range(data_len//2):
        if(input_data[i] != input_data[data_len-1-i]):
            is_felindrom = False
    return is_felindrom

def make_felindrom(input_data, zfill_len):
    original = input_data
    while felindrom_check(str(input_data)) != True:
        input_data = int(input_data) + 1
        input_data = str(input_data).zfill(zfill_len)
        
    return int(input_data) - int(original)

if __name__ == "__main__" : 
    while True:
        is_felindrom = False
        input_data = input()
        zfill_len = len(input_data)

        if(input_data == '0'):
            break
        is_felindrom = felindrom_check(input_data)
        if(is_felindrom == False):
            min_felindrom = make_felindrom(input_data, zfill_len)
            print(min_felindrom)
        else:
            print("0")

        
        
