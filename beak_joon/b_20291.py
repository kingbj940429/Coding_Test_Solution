''' 20291번 파일 정리 '''
import sys
input = sys.stdin.readline

N = int(input())
dic = {}
ext_list = []
for _ in range(N):
    temp = input().rstrip().split('.')
    if temp[1] not in dic :
        dic[temp[1]] = 1
    else:
        dic[temp[1]] += 1
    ext_list.append(temp[1])
ext_list = list(set(ext_list))
ext_list.sort()

for i in ext_list:
    print(i, dic.get(i))
