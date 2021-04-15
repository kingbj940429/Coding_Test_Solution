''' 10817번 세 수 '''

datas = list(input().split(" "))
datas = list(map(int, datas))
datas.sort()
print(datas[-2])