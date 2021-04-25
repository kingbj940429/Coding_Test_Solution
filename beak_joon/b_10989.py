''' 10989번 수 정렬하기 3 '''
import sys
input = sys.stdin.readline
N = int(input().rstrip())

count = [0] * 10001
for _ in range(N):
    temp = int(input().rstrip())
    count[temp] += 1 # Increase the value in the index.


for i in range(len(count)): # Check the sort information recorded on the list.
    for j in range(count[i]):
        print(i) # Print each index as many times as it appears.