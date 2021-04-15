''' 1966번 프린터 큐 '''

from collections import deque

def first_to_end(printer):
    temp = printer.popleft()
    printer.append(temp)

    return printer

def index_list(printer):
    index = []
    for i in range(len(printer)):
        index.append(i)
    return index


if __name__ == "__main__" : 
    K = int(input())

    for _ in range(K):
        #인쇄수, 출력하려는 인쇄물 인덱스
        N,M = map(int,input().split())
        printer = deque(list(map(int, input().split())))
        cnt = 0    
        #인쇄 순서가 키, 인쇄 중요도가 값
        index = deque(index_list(printer))
        max_value = max(printer)

        
        while True:
            if(int(max_value) > int(printer[0])):
                index = first_to_end(index)
                printer = first_to_end(printer)
            else:
                printer[0] = 0
                max_value = max(printer)
                cnt += 1
                if(index[0] == M):
                    break
                index = first_to_end(index)
                printer = first_to_end(printer)

                
        print(cnt)
                
                




        

        

        


      
        