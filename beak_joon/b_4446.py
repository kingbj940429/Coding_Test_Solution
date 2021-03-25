''' 4446번 ROT13 '''
import sys
mom_chars = ['a', 'i', 'y', 'e', 'o', 'u']
child_chars = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
if __name__ == "__main__" :
    flag = True
    while flag == True:
        input_data = sys.stdin.readline()
        result = ""
        len_mom_chars = len(mom_chars)
        len_child_chars = len(child_chars)
        for i in range(len(input_data)):
            print(ord(input_data[i]))
            if(ord(input_data[i]) < 32 or ord(input_data[i]) > 126):
                if(ord(input_data[i]) != 10):
                    flag = False
                    break
            #대문자이고 모음이라면
            if(input_data[i].isupper() == True):
                data = input_data[i].lower()
                if(data in mom_chars):
                    index = mom_chars.index(data)
                    result += mom_chars[(index + 3)%len_mom_chars].upper()
                else:
                    index = child_chars.index(data)
                    result += child_chars[(index + 10)%len_child_chars].upper()
            elif(input_data[i] in mom_chars):
                index = mom_chars.index(input_data[i])
                result += mom_chars[(index + 3)%len_mom_chars]
            elif(input_data[i] in child_chars):
                index = child_chars.index(input_data[i])
                result += child_chars[(index + 10)%len_child_chars]
            else:
                result += input_data[i]
        print(result)
