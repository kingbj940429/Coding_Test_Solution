''' 11004번 K번째 수 '''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

datas = list(map(int,input().split()))

datas.sort()

print(datas[K-1])