''' 11656번 접미사 배열 '''
from collections import deque

if __name__ == "__main__":
    input_data = list(input())
    misa_list = []
    temp = input_data

    for _ in range(len(input_data)):
        misa_list.append("".join(list(temp)))
        temp = deque(temp)
        temp.popleft()

    misa_list.sort()
    
    for val in misa_list:
        print(val)