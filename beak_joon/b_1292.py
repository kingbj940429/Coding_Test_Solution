''' 1292번 쉽게 푸는 문제 '''

A, B = map(int,input().split())

num = 1
string_num = []
while True:
    for i in range(num):
        string_num.append(num)
    num += 1
    if(len(string_num) > B):
        break

start = A-1
end = B-1

result = 0
for i in range(start, end+1):
    result += int(string_num[i])
print(result)