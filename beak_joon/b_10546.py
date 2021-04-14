''' 10546번 배부른 마라토너 '''

import sys
input = sys.stdin.readline
if __name__ == "__main__" :
    N = int(input())

    maratoners = {}

    for _ in range(N):
        temp = input().rstrip()
        if(temp not in maratoners):
            maratoners[temp] = 1
        else:
            maratoners[temp] += 1
    
    for _  in range(N-1):
        temp = input().rstrip()
        if(temp in maratoners):
            maratoners[temp] -= 1
    
    for key in maratoners.keys():
        if(maratoners[key] == 1):
            print(key)
    