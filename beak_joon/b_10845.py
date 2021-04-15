''' 10845번 큐 '''
from collections import deque

import sys
input = sys.stdin.readline

if __name__ == "__main__" :
    N = int(input().rstrip())
    que = deque([])

    for _ in range(N):
        command = list(input().rstrip().split())
        
        if(command[0] == 'push'):
            que.append(command[1])
        elif(command[0] == 'front'):
            if(len(que) < 1):
                print(-1)
            else:
                print(que[0])
        elif(command[0] == 'back'):
            if(len(que) < 1):
                print(-1)
            else:
                print(que[-1])
        elif(command[0] == 'pop'):
            if(len(que) < 1):
                print(-1)
            else:
                print(que.popleft())
        elif(command[0] == 'size'):
            print(len(que))
        elif(command[0] == 'empty'):
            if(len(que) < 1):
                print(1)
            else:
                print(0)
