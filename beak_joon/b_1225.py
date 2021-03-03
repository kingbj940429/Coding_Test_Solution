# if __name__ == "__main__":
#     input_data = list(input().split(" "))

#     A = input_data[0]
#     B = input_data[1]
#     result = 0

#     for a in A:
#         for b in B:
#             result = result + int(a)*int(b)
    
#     print(result)
''' 위 코드는 시간 초과 걸려서 다시 품'''

if __name__ == "__main__":
    input_data = list(input().split(" "))

    A = input_data[0]
    B = input_data[1]
    A_temp , B_temp= 0, 0

    for a in A :
        A_temp +=int(a)
    for b in B :
        B_temp +=int(b)

    print(A_temp * B_temp)
        