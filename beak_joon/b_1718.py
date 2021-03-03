''' 1718번 암호 '''
def alphas():
    start = ord("a")
    end = ord("z")

    for i in range(start, end+1):
        alpha_list[i - ord("a")+1]=chr(i)

def on_encrption():

    return False

alpha_list = {}
if __name__ == "__main__":
    result = []
    normal = input()
    encrypt = input()
    alphas()#1~26으로 알파벳 재정의

    for i in range(len(normal)):
        if(normal[i].isspace() == True):
            result.append(" ")
            continue
        enc_key = encrypt[i%len(encrypt)]
        enc_val = ord(normal[i]) - ord(enc_key)

        if(enc_val <= 0 ):
            enc_val = enc_val + 26
        result.append(alpha_list.get(enc_val))   
    print("".join(result))


    
