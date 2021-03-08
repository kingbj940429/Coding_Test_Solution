'''2715번 수 정렬하기2 '''

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()
for i in l:
    sys.stdout.write(str(i)+'\n')
    