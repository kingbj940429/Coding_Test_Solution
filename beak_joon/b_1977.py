''' 1977번 완전제곱수 '''
from math import sqrt
if __name__ == "__main__":
    M = int(input())
    N = int(input())

    result = 0
    result_list = []
    for i in range(M, N+1):
        temp = str(sqrt(i)).split(".")
        if(len(temp[1]) < 2):
            result += i
            result_list.append(i)

    if(len(result_list) > 0):
        print(result)
        print(result_list[0])
    else:
        print(-1)

        


    
