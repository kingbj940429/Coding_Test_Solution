''' 1920번 수 찾기 '''
import sys
input = sys.stdin.readline

def binary_search(array, target, start,end):
    while start<=end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


#N 관련
N = int(input())
N_list = sorted(list(map(int,input().split())))

#M 관련
M = int(input())
M_list = list(map(int,input().split()))

start = 0
end = len(N_list) - 1

for i in M_list:
    print(binary_search(N_list,i,start,end))