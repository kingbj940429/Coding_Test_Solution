''' 두 배열의 원소 교체 '''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

for i in range(K):
    A[i], B[N-i-1] = B[N-i-1], A[i]

print(sum(A))
    
        


    


