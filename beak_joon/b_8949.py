''' 8949번 대충 더해 '''
''' deque 사용 '''
from collections import deque
if __name__ == "__main__":
    input_data = input().split()

    A = deque(input_data[0])
    B = deque(input_data[1])

    if(len(A) > len(B)):
        max_len = len(A)
        min_len = len(B)
    else:
        max_len = len(B)
        min_len = len(A)

    diff_AB = max_len - min_len

    for _ in range(diff_AB):
        if(len(A) > len(B)):
            B.appendleft("0")
        else:
            A.appendleft("0")
    
    A = list(A)
    B = list(B)
    result = ""
    for i in range(len(A)):
        result += str(int(A[i]) + int(B[i]))
    print(result)
    




    